import numpy as np


def trimf(universe, points):
	a, b, c = points
	membership = np.zeros_like(universe, dtype=float)
	rising = (universe > a) & (universe < b)
	falling = (universe > b) & (universe < c)
	membership[rising] = (universe[rising] - a) / (b - a)
	membership[falling] = (c - universe[falling]) / (c - b)
	membership[universe == b] = 1.0
	return membership


def trapmf(universe, points):
	a, b, c, d = points
	membership = np.zeros_like(universe, dtype=float)

	if a == b:
		membership[universe <= b] = 1.0
	else:
		membership[(universe >= a) & (universe < b)] = (
			(universe[(universe >= a) & (universe < b)] - a) / (b - a)
		)

	membership[(universe >= b) & (universe <= c)] = 1.0

	if c == d:
		membership[universe >= c] = 1.0
	else:
		falling = (universe > c) & (universe <= d)
		membership[falling] = (d - universe[falling]) / (d - c)

	return membership


density_universe = np.arange(0, 51, 1)
waiting_universe = np.arange(0, 121, 1)
green_universe = np.arange(10, 91, 1)

density_sets = {
	"low": trapmf(density_universe, [0, 0, 10, 15]),
	"medium": trimf(density_universe, [10, 20, 30]),
	"high": trapmf(density_universe, [25, 50, 50, 50]),
}

waiting_sets = {
	"short": trapmf(waiting_universe, [0, 0, 20, 30]),
	"moderate": trimf(waiting_universe, [20, 50, 80]),
	"long": trapmf(waiting_universe, [70, 120, 120, 120]),
}

green_sets = {
	"short": trapmf(green_universe, [10, 10, 20, 30]),
	"medium": trimf(green_universe, [30, 45, 60]),
	"long": trapmf(green_universe, [60, 75, 90, 90]),
}

rules = [
	("low", "short", "short"),
	("low", "moderate", "short"),
	("low", "long", "medium"),
	("medium", "short", "short"),
	("medium", "moderate", "medium"),
	("medium", "long", "long"),
	("high", "short", "medium"),
	("high", "moderate", "long"),
	("high", "long", "long"),
]


def membership_at(value, universe, membership):
	return np.interp(value, universe, membership)


def green_time(traffic_density, waiting_time):
	if not 0 <= traffic_density <= 50:
		raise ValueError("Traffic density must be between 0 and 50.")
	if not 0 <= waiting_time <= 120:
		raise ValueError("Waiting time must be between 0 and 120.")

	density_degrees = {
		name: membership_at(traffic_density, density_universe, values)
		for name, values in density_sets.items()
	}
	waiting_degrees = {
		name: membership_at(waiting_time, waiting_universe, values)
		for name, values in waiting_sets.items()
	}
	combined_output = np.zeros_like(green_universe, dtype=float)

	for density_name, waiting_name, green_name in rules:
		strength = min(
			density_degrees[density_name],
			waiting_degrees[waiting_name],
		)
		clipped_output = np.minimum(strength, green_sets[green_name])
		combined_output = np.maximum(combined_output, clipped_output)

	area = np.sum(combined_output)
	if area == 0:
		raise ValueError("No fuzzy rules fired for these inputs.")

	return np.sum(green_universe * combined_output) / area


test_cases = [(5, 10), (20, 50), (45, 110), (35, 100)]
for traffic_density, waiting_time in test_cases:
	duration = green_time(traffic_density, waiting_time)
	print(
		f"density={traffic_density}, waiting={waiting_time} "
		f"-> green={duration:.1f} s"
	)


density_values = np.arange(0, 51, 10)
waiting_values = np.arange(0, 121, 20)
control_surface = np.array(
	[
		[green_time(density, waiting) for density in density_values]
		for waiting in waiting_values
	]
)
print("\nControl surface (rows: waiting time, columns: density):")
print("Density:", density_values)
for waiting, row in zip(waiting_values, control_surface):
	print(f"Waiting {waiting:3d} s:", np.round(row, 1))
