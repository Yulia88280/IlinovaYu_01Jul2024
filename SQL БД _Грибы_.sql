/*Выберите уникальные регионы сбора грибов.*/
SELECT DISTINCT name 
FROM regions;

/*Выведите название, сезон сбора и съедобность грибов,  которые относятся к категории “Трубчатые”.*/
SELECT m.name, m.season, m.edible 
FROM mushrooms m 
JOIN categories c ON m.category_id = c.category_id 
WHERE c.name = 'Трубчатые';

/*Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.*/
SELECT c.name AS category_name, COUNT(m.mushroom_id) AS mushroom_count 
FROM mushrooms m 
JOIN categories c ON m.category_id = c.category_id 
GROUP BY c.name 
ORDER BY mushroom_count DESC;

/*Выведите название и описание съедобных грибов, которые лучше всего собирать в 5 самых больших по размеру (size) регионах.*/
SELECT m.name, m.description 
FROM mushrooms m 
JOIN regions r ON m.primary_region_id = r.region_id 
WHERE m.edible = TRUE 
ORDER BY r.size DESC 
LIMIT 5;

/*Выведите названия всех грибов, которые растут весной, относятся к категории “Пластинчатые”  и их лучше всего собирать в местах размером до 6000 условных единиц (size)*/
SELECT m.name 
FROM mushrooms m 
JOIN categories c ON m.category_id = c.category_id 
JOIN regions r ON m.primary_region_id = r.region_id 
WHERE m.season = 'Весна' 
AND c.name = 'Пластинчатые' 
AND r.size <= 6000;