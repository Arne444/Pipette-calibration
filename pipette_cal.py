# Pipette-calibration
# Distribute known volumes of liquid to tubes for pipette calibration

from opentrons import robot, containers, instruments

p200rack = containers.load('tiprack-200ul', 'A1', 'p200-rack')

p200_tube_rack = containers.load('tube-rack-2ml', 'B3', 'p200-tube-rack')
trash = containers.load('trash-box', 'A3', 'trash')
trough = containers.load('trough-12row', 'C1', 'source-trough')

#Create 3x6 2ml tube rack for DNA samples
containers.create(
	'3x6-tube-rack-2ml',
	grid=(3,6),
	spacing=(19.5,19.5),
	diameter=9.5,
	depth=40
)

p20_tube_rack = containers.load('3x6-tube-rack-2ml', 'B2', 'p20-tube-rack')

#Create 6x12 p20 tip rack container
containers.create(
	'tiprack-200ul-6x12',
	grid=(6,12),
	spacing=(9, 9),
	diameter=5,
	depth=60
)

p20rack = containers.load('tiprack-200ul-6x12', 'E1', 'p20-rack')

p20 = instruments.Pipette(
	trash_container=trash,
	tip_racks=[p20rack],
	min_volume=2,
	max_volume=20,
	axis="a"
)

p200 = instruments.Pipette(
	trash_container=trash,
	tip_racks=[p200rack],
	min_volume=20,
	max_volume=200,
	axis="b"
)

source_trough = trough.wells('A1')

output200 = [well.bottom() for well in p200_tube_rack.wells('A1', to= 'A2')]
output150 = [well.bottom() for well in p200_tube_rack.wells('B2', to= 'B3')]
output50 = [well.bottom() for well in p200_tube_rack.wells('C3', to= 'C4')]
output20 = [well.bottom() for well in p200_tube_rack.wells('D4', to= 'D5')]

output20_1 = [well.bottom() for well in p200_tube_rack.wells('A6', to= 'B6')]
output20_2 = [well.bottom() for well in p20_tube_rack.wells('A1', to= 'C1')]
output15 = [well.bottom() for well in p20_tube_rack.wells('A2', to= 'B3')]
output5 = [well.bottom() for well in p20_tube_rack.wells('C3', to= 'A5')]
output2 = [well.bottom() for well in p20_tube_rack.wells('B5', to= 'C6')]

p20.transfer(
	5, source_trough, output5, blow_out=True)

p20.transfer(
	2, source_trough, output2, blow_out=True)