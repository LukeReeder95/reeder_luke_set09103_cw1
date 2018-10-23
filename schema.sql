DROP TABLE if EXISTS drivers;
DROP TABLE if EXISTS blades;

CREATE TABLE drivers (
    name text,
    description text
);

CREATE TABLE blades (
    role text,
    name text,
    element text,
    weapon text,
    description text
);


insert into blades values ("Dps", "Pyra", "Fire", "Unique", "Story blade, unique weapon is Aegis Sword, can only be used by Rex as a driver");
insert into blades values ("Dps", "Mythra", "Light", "Unique", "Story blade, unique weapon is Aegis Sword, can only be used by Rex as a driver");
insert into blades values ("Healer", "Dromarch", "Water", "Twin Rings", "Story blade, only usable by Nia as a driver");
insert into blades values ("Tank", "Poppi", "Earth", "Unique", "Story blade, only usable by Tora as a driver, artificial blade, can be customised");
insert into blades values ("Tank", "Brighid", "Fire", "Unique", "Story blade, only usable by Morag as a driver, Unique weapon is Whip Swords");
insert into blades values ("Dps", "Pandoria", "Electric", "Unique", "Story blade, only usable by Zeke as a driver, unique weapon is Big Bang Edge");
insert into blades values ("Dps", "Kos-Mos", "Light", "Ether Cannon", "Rare blade obtainable through core crystals, can be used by any driver");
insert into blades values ("Healer", "Boreas", "Wind", "Bit-Ball", "Rare blade obtainable through core crystals, can be used by any driver");
insert into blades values ("Healer", "Dahlia", "Ice", "Bit-Ball", "Rare blade obtainable through core crystals, can be used by any driver");
insert into blades values ("Dps", "Zenobia", "Wind", "Great Axe", "Rare blade, obtainable through core crystals, can be used by any driver, extremely good for challenging super bosses");
insert into blades values ("Dps", "Agate", "Earth", "Great Axe", "Rare blade, obtainable through core crystals, can be used by any driver");
insert into blades values ("Tank", "Kasandra", "Dark", "Shield Hammer", "Rare blade, obtainable through defeating unique monster, can be used by any driver");
insert into blades values ("Tank", "Electra", "Electric", "Shield Hammer", "Rare blade, obtainable through core crystals, can be used by any driver");
insert into blades values ("Dps", "Herald", "Electric", "Ether Cannon", "Rare blade obtained through a quest in tantal, can be used by any driver");
insert into blades values ("Healer", "Kora", "Electric", "Knuckle Claws", "Rare blade obtained through core crystals, can be used by any driver");
insert into blades values ("Healer", "Ursula", "Ice", "Knucle Claws", "Rare blade obtained through core crystals, can be used by any driver");
insert into blades values ("Healer", "Nim", "Earth", "Knuckle Claws", "Rare blade obtained through core crystals, can be used by any driver");
insert into blades values ("Dps", "Perun", "Ice", "Mega Lance", "Rare blade obtained through core crystals, can be used by any driver");
insert into blades values ("Dps", "Praxis", "Water", "Mega Lance", "Rare blade obtained through side quest line, can be used by any driver");

insert into drivers values ("Rex", "Main playable character, avalible from the start, main blade is Pyra");
insert into drivers values ("Nia", "Nia is a driver that becomes avalible in chapter 2, she is primarily a healer based driver due to her main blade being Dromarch, a healer blade");
insert into drivers values ("Morag", "Morag is a driver that becomes avalible in chapter 4, she is primarily a tank based driver due to her story blade being Bridhid, a tank blade");
insert into drivers values ("Tora", "Tora is a special driver due to his inability to use normal blades. Because of this, he designed and built his own artificial blade; Poppi");
insert into drivers values ("Zeke", "Zeke is the final driver that becomes avalible in chapter 7. Zeke is primarily a dps style driver with his main blade being Pandoria");
