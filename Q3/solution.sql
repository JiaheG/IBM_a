select o.owner_id, o.owner_name, count(cam.category_id) different_category_count
from owner o, article a, category_article_mapping cam
where a.category_id = cam.category_id and a.owner_id = o.owner_id
group by  o.owner_id
order by  different_category_count desc;
