INSERT INTO gtairportnavigation.node
	(id, name, type, floor)
VALUES
	('TXN', 'T Concourse', 0, 1),
	('TN', '', 0, 1),
	('TR24', 'News Express', 5, 1),
	('TG9', 'Gate T9', 2, 1),
	('TSN', 'T Concourse', 0, 1),
	('TJ1', '', 0, 1),
	('TF12', 'Burger King', 4, 1),
	('TR16', 'Travel Size Essentials', 5, 1),
	('TR19', 'BestBuy Zoom', 5, 1),
	('TJ2', '', 0, 1),
	('TR29', 'Z Market', 5, 1),
	('TJ3', '', 0, 1),
	('TG10', 'Gate T10', 2, 1),
	('TJ4', '', 0, 1),
	('TCAA', 'American Airlines Club', 7, 1),
	('TJ5', '', 0, 1),
	('TG11', 'Gate T11', 2, 1),
	('TJ6', '', 0, 1),
	('TF6', 'Goldberg\'s Bagels', 4, 1),
	('TJ7', '', 0, 1),
	('TG12', 'Gate T12', 2, 1),
	('TR26', 'Southern Flavors', 5, 1),
	('TF11', 'Vending Machines', 4, 1),
	('TJ8', '', 0, 1),
	('TF8', 'Saucy Blues', 4, 1),
	('TR17X1', 'Atlanta News and Gifts', 5, 1),
	('TJ9', '', 0, 1),
	('TG13', 'Gate T13', 2, 1),
	('TJ10', '', 0, 1),
	('TG14', 'Gate T14', 2, 1),
	('TG15', 'Gate T15', 2, 1),
	('TM', 'T Concourse', 0, 1),
	('TXS', 'T Concourse', 0, 1),
	('TS', '', 0, 1),
	('TR25X1', 'Shellis News', 5, 1),
	('TR28', 'Tech Showcase', 5, 1),
	('TJ11', '', 0, 1),
	('TG8', 'Gate T8', 2, 1),
	('TR21', 'Headphone Hub', 5, 1),
	('TR22', 'Inmotion Entertainment', 5, 1),
	('TJ12', '', 0, 1),
	('TF7', 'Sam Adams / Checkpoint Bistro', 4, 1),
	('TJ13', '', 0, 1),
	('TG7', 'Gate T7', 2, 1),
	('TJ14', '', 0, 1),
	('TF1', 'Bojangles', 4, 1),
	('TCD', 'Delta Sky Club', 7, 1),
	('TJ15', '', 0, 1),
	('TF5', 'Famous Famiglia', 4, 1),
	('TF3', 'The Coffee Bean and Tea Leaf', 4, 1),
	('TJ16', '', 0, 1),
	('TG6', 'Gate T6', 2, 1),
	('TJ17', '', 0, 1),
	('TR23', 'Lather', 5, 1),
	('TJ18', '', 0, 1),
	('TR27', 'Talie', 5, 1),
	('TG5', 'Gate T5', 2, 1),
	('TJ19', '', 0, 1),
	('TR17X2', 'Atlanta News and Gifts', 5, 1),
	('TJ20', '', 0, 1),
	('TR20', 'Brookstone', 5, 1),
	('TJ21', '', 0, 1),
	('TG4', 'Gate T4', 2, 1),
	('TJ22', '', 0, 1),
	('TF9', 'TJI Friday\'s', 4, 1),
	('TJ23', '', 0, 1),
	('TF10', 'Jamba Juice', 4, 1),
	('TJ24', '', 0, 1),
	('TF4', 'Corner Bakery Cafe', 4, 1),
	('TJ25', '', 0, 1),
	('TG3', 'Gate T3', 2, 1),
	('TR18', 'B Iconic', 5, 1),
	('TJ26', '', 0, 1),
	('TR25X2', 'Shellis News', 5, 1),
	('TJ27', '', 0, 1),
	('TG2', 'Gate T2', 2, 1),
	('TG1', 'Gate T1', 2, 1),
	('DTXN1', '', 9, 1),
	('DTXN2', '', 9, 1),
	('DTXN3', '', 9, 1),
	('DTXN4', '', 9, 1),
	('DTXN5', '', 9, 1),
	('DTXN6', '', 9, 1),
	('DTXS1', '', 9, 1),
	('DTXS2', '', 9, 1),
	('DTXS3', '', 9, 1),
	('DTXS4', '', 9, 1),
	('DTXS5', '', 9, 1),
	('DTXS6', '', 9, 1),
	('DTXW1', '', 9, 1),
	('DTXW2', '', 9, 1),
	('DTXMN', '', 9, 1),
	('DTXMS', '', 9, 1),
	('DTJ1', '', 0, 1),
	('DTJ2', '', 0, 1),
	('DTJ3', '', 0, 1),
	('DTJ4', '', 0, 1),
	('DTJ5', '', 0, 1),
	('DTJ6', '', 0, 1),
	('DTJ7', '', 0, 1),
	('DTJ8', '', 0, 1),
	('DTJ9', '', 0, 1),
	('DTJ10', '', 0, 1),
	('DTJ11', '', 0, 1),
	('DTJ12', '', 0, 1),
	('DTJ13', '', 0, 1),
	('DTJ14', '', 0, 1),
	('DTJ15', '', 0, 1),
	('DTJ16', '', 0, 1),
	('DTJ17', '', 0, 1),
	('DTSN', 'North Security', 1, 1),
	('DTSM', 'Main Security', 1, 1),
	('DTSS', 'South Security', 1, 1);

INSERT INTO gtairportnavigation.neighbor
	(from_node_id, to_node_id, distance, angle, type)
VALUES
	('TXN', 'TN', 100, 90, 0),
	('TN', 'TR24', 0, 180, 0),
	('TN', 'TG9', 0, 90, 0),
	('TN', 'TJ1', 100, 0, 0),
	('TJ1', 'TF12', 0, 90, 0),
	('TJ1', 'TR16', 0, 270, 0),
	('TJ1', 'TR19', 0, 270, 0),
	('TJ1', 'TJ2', 100, 0, 0),
	('TJ2', 'TR29', 0, 90, 0),
	('TJ2', 'TJ3', 100, 0, 0),
	('TJ3', 'TG10', 0, 90, 0),
	('TJ3', 'TJ4', 100, 0, 0),
	('TJ4', 'TCAA', 0, 270, 0),
	('TJ4', 'TJ5', 100, 0, 0),
	('TJ5', 'TG11', 0, 90, 0),
	('TJ5', 'TJ6', 100, 0, 0),
	('TJ6', 'TF6', 0, 90, 0),
	('TJ6', 'TJ7', 100, 0, 0),
	('TJ7', 'TG12', 0, 90, 0),
	('TJ7', 'TR26', 0, 270, 0),
	('TJ7', 'TF11', 0, 270, 0),
	('TJ7', 'TJ8', 100, 0, 0),
	('TJ8', 'TF8', 0, 90, 0),
	('TJ8', 'TR17X1', 0, 90, 0),
	('TJ8', 'TJ9', 100, 0, 0),
	('TJ9', 'TG13', 0, 90, 0),
	('TJ9', 'TJ10', 100, 0, 0),
	('TJ10', 'TG14', 0, 90, 0),
	('TJ10', 'TG15', 100, 0, 0),

	('TN', 'TM', 100, 180, 0),
	('TM', 'TS', 100, 180, 0),
	('TXS', 'TS', 100, 90, 0),
	('TXS', 'TR25X1', 0, 0, 0),
	('TXS', 'TR28', 0, 0, 0),
	('TS', 'TJ11', 100, 180, 0),
	('TJ11', 'TG8', 0, 90, 0),
	('TJ11', 'TR21', 0, 270, 0),
	('TJ11', 'TR22', 0, 270, 0),
	('TJ11', 'TJ12', 100, 180, 0),
	('TJ12', 'TF7', 0, 270, 0),
	('TJ12', 'TJ13', 100, 180, 0),
	('TJ13', 'TG7', 0, 90, 0),
	('TJ13', 'TJ14', 100, 180, 0),
	('TJ14', 'TF1', 0, 270, 0),
	('TJ14', 'TCD', 0, 90, 0),
	('TJ14', 'TJ15', 100, 180, 0),
	('TJ15', 'TF5', 0, 270, 0),
	('TJ15', 'TF3', 0, 90, 0),
	('TJ15', 'TJ16', 100, 180, 0),
	('TJ16', 'TG6', 0, 90, 0),
	('TJ16', 'TJ17', 100, 180, 0),
	('TJ17', 'TR23', 0, 270, 0),
	('TJ17', 'TJ18', 100, 180, 0),
	('TJ18', 'TR27', 0, 270, 0),
	('TJ18', 'TG5', 0, 90, 0),
	('TJ18', 'TJ19', 100, 180, 0),
	('TJ19', 'TR17X2', 0, 270, 0),
	('TJ19', 'TJ20', 100, 180, 0),
	('TJ19', 'TR20', 0, 270, 0),
	('TJ20', 'TJ21', 100, 180, 0),
	('TJ21', 'TG4', 0, 90, 0),
	('TJ21', 'TJ22', 100, 180, 0),
	('TJ22', 'TF9', 0, 270, 0),
	('TJ22', 'TJ23', 100, 180, 0),
	('TJ22', 'TF10', 0, 270, 0),
	('TJ23', 'TJ24', 100, 180, 0),
	('TJ22', 'TF4', 0, 270, 0),
	('TJ24', 'TJ25', 100, 180, 0),
	('TJ25', 'TG3', 0, 90, 0),
	('TJ25', 'TR18', 0, 270, 0),
	('TJ25', 'TJ26', 100, 180, 0),
	('TJ26', 'TR25X2', 0, 270, 0),
	('TJ26', 'TJ27', 100, 180, 0),
	('TJ27', 'TG2', 0, 90, 0),
	('TJ27', 'TG1', 0, 135, 0),
	('DTXN6', 'DTSN', 100, 135, 0),
	('DTXN5', 'DTJ1', 100, 180, 0),
	('DTXN4', 'DTJ3', 100, 135, 0),
	('DTXN3', 'DTJ4', 100, 135, 0),
	('DTXN2', 'DTJ5', 100, 180, 0),
	('DTXN1', 'DTJ5', 100, 135, 0),
	('DTJ1', 'DTSN', 100, 90, 0),
	('DTJ2', 'DTJ1', 100, 90, 0),
	('DTJ3', 'DTJ2', 100, 90, 0),
	('DTJ4', 'DTJ3', 100, 90, 0),
	('DTJ5', 'DTJ4', 100, 90, 0),
	('DTJ6', 'DTJ5', 100, 90, 0),
	('DTXW1', 'DTJ6', 100, 90, 0),
	('DTJ6', 'DTXMN', 100, 180, 0),
	('DTJ7', 'DTSM', -1, 270, 0),
	('DTSM', 'DTJ8', 100, 270, 0),
	('DTJ8', 'DTJ9', 100, 270, 0),
	('DTJ9', 'DTJ10', 100, 270, 0),
	('DTJ10', 'DTJ11', 100, 270, 0),
	('DTJ2', 'DTJ8', 100, 180, 0),
	('DTJ3', 'DTJ9', 100, 135, 0),
	('DTJ4', 'DTJ10', 100, 180, 0),
	('DTJ5', 'DTJ11', 100, 180, 0),
	('DTJ8', 'DTJ13', 100, 180, 0),
	('DTJ9', 'DTJ14', 100, 225, 0),
	('DTJ10', 'DTJ15', 100, 180, 0),
	('DTJ11', 'DTJ16', 100, 180, 0),
	('DTJ12', 'DTSS', 100, 90, 0),
	('DTJ13', 'DTJ12', 100, 90, 0),
	('DTJ14', 'DTJ13', 100, 90, 0),
	('DTJ15', 'DTJ14', 100, 90, 0),
	('DTJ16', 'DTJ15', 100, 90, 0),
	('DTJ17', 'DTJ16', 100, 90, 0),
	('DTJ17', 'DTXMS', 100, 0, 0),
	('DTXW2', 'DTJ17', 100, 90, 0),
	('DTXS1', 'DTJ12', 100, 0, 0),
	('DTXS2', 'DTJ13', 100, 0, 0),
	('DTXS3', 'DTJ14', 100, 0, 0),
	('DTXS4', 'DTJ15', 100, 0, 0),
	('DTXS5', 'DTJ15', 100, 45, 0),
	('DTXS6', 'DTJ16', 100, 45, 0),

	('DTSN', 'TXN', 0, 90, 9),
	('DTSS', 'TXS', 0, 90, 9);
