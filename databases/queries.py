GET_CHARACTERS = '''
    SELECT * FROM charactercreator_character;
'''

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight 
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id
'''

TOTAL_CHARACTERS = '''
    SELECT COUNT(*) FROM charactercreator_character;
'''

TOTAL__NECRO_SUBCLASS = '''
    SELECT COUNT(*) FROM charactercreator_necromancer;
'''

TOTAL_MAGE_SUBCLASS = '''
    SELECT COUNT(*) FROM charactercreator_mage;
'''

TOTAL_FIGHTER_SUBCLASS = '''
    SELECT COUNT(*) FROM charactercreator_fighter;
'''

TOTAL_THIEF_SUBCLASS = '''
    SELECT COUNT(*) FROM charactercreator_thief;
'''

TOTAL_CLERIC_SUBCLASS = '''
    SELECT COUNT(*) FROM charactercreator_cleric;
'''

TOTAL_ITEMS = '''
    SELECT COUNT(*) FROM armory_item;
'''

WEAPONS = '''
    SELECT COUNT(*) FROM armory_weapon;
'''

NON_WEAPONS = '''
    SELECT COUNT(*) FROM armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    WHERE aw.power IS NULL;
'''

CHARACTER_ITEMS = '''
    SELECT COUNT(item_id) FROM charactercreator_character AS cc_char
    INNER JOIN charactercreator_character_inventory as cc_inv
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;
'''

CHARACTER_WEAPONS = '''
    SELECT COUNT(ai.item_id) AS total_weapons
    FROM armory_item as ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    GROUP BY character_id
    LIMIT 20;
'''

AVG_CHARACTER_ITEMS = '''
    SELECT AVG(total_items)
    FROM (SELECT name, COUNT(item_id) AS total_items
    FROM charactercreator_character as cc_char
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id);
'''

AVG_CHARACTER_WEAPONS = '''
    SELECT AVG (total_weapons)
    FROM (SELECT COUNT(ai.item_id) AS total_weapons
    FROM armory_item as ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    GROUP BY character_id);
'''

QUERY_LIST = [TOTAL_CHARACTERS, 
              TOTAL__NECRO_SUBCLASS, 
              TOTAL_MAGE_SUBCLASS, 
              TOTAL_THIEF_SUBCLASS, 
              TOTAL_CLERIC_SUBCLASS, 
              TOTAL_FIGHTER_SUBCLASS, 
              TOTAL_ITEMS, 
              WEAPONS, 
              NON_WEAPONS, 
              CHARACTER_ITEMS, 
              CHARACTER_WEAPONS]

CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL, 
    "age" INT NOT NULL, 
    "country_of_origin" VARCHAR(200) NOT NULL);
'''

INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Ian Evans', 30, 'USA');
'''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters
'''

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table
'''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    ("character_id" SERIAL NOT NULL PRIMARY KEY, 
    "name" VARCHAR(30) NOT NULL, 
    "level" INT NOT NULL, 
    "exp" INT NOT NULL, 
    "hp" INT NOT NULL, 
    "strength" INT NOT NULL, 
    "intelligence" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

CREATE_IAN = '''
INSERT INTO characters
("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom", 
VALUES ('Ian Evans', 50, 100, 1000, 9000, 40, 50, 120)
);
'''