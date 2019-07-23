use sakila;

-- Part 1 --

select first_name, last_name from actor;

alter table actor
	add column `Actor Name` varchar(50);
	update actor set `Actor Name` = concat (first_name, ' ', last_name);
    
select * from actor;

-- Part 2 --

select actor_id, first_name, last_name from actor
	where first_name = 'joe';
    
select * from actor
	where last_name like '%GEN%';
    
select * from actor
	where last_name like '%LI%'
    order by last_name, first_name;
    
select country_id, country from country
where country  in ('Afghanistan', 'Bangladesh', 'China');

-- Part 3 --

alter table actor
	add column Description blob;

select * from actor;

alter table actor
	drop column description;
    
select * from actor;

-- Part 4 --

select last_name, count(*) as count from actor
	group by last_name;
    
select last_name, count(*) as count from actor
	group by last_name
    having count(*) > 1 ;

update actor    
	set first_name = 'HARPO'
	where first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

select * from actor
	where first_name = 'HARPO' AND last_name = 'WILLIAMS';
    
update actor
	set first_name = 'GROUCHO'
	where first_name = 'HARPO';
    
select * from actor
	where first_name = 'GROUCHO' AND last_name = 'WILLIAMS';
    
-- Part 5 maybe correct unsure? --

SHOW CREATE TABLE address;

-- Part 6 --

select staff.first_name, staff.last_name, address.address
	from staff
    inner join address on staff.address_id = address.address_id;
    
select staff.first_name, staff.last_name, sum(payment.amount) as `Total Amount`
	from staff
    inner join payment on staff.staff_id = payment.staff_id
    where payment.payment_date like "2005-08%"
    group by first_name;
    
select film.title, count(film_actor.film_id) as 'Number of Actors'
	from film
    inner join film_actor on film.film_id = film_actor.film_id
    group by title;
    
select film.title, count(film.film_id) as '# in stock'
	from film
    inner join inventory on film.film_id = inventory.film_id
    where title = 'Hunchback Impossible'
    group by title;
    
select customer.first_name, customer.last_name, sum(payment.amount) as 'Total Amount Paid'
	from payment
    inner join customer on payment.customer_id = customer.customer_id
    group by first_name
    order by last_name;
    
-- Part 7 --

select title as 'Film Title'
	from film
	where title like ('K%') or title like ('Q%') and language_id in (
		select language_id from language
        where name = 'English');
        
	select title as 'Film Title'
	from film
	where title like ('K%') or title like ('Q%') and language_id in (
		select language_id from language
        where name = 'English');
        
	select `Actor Name` from actor
    where actor_id in (
		select actor_id from film_actor
        where film_id in (
			select film_id from film
            where title = 'Alone Trip'));
            
select customer.first_name, customer.last_name, customer.email from customer
left join address on address.address_id = customer.address_id
left join city on city.city_id = address.city_id
left join country on country.country_id = city.country_id
where country = 'Canada';

select title as 'Title' from film
left join film_category on film_category.film_id = film.film_id
left join category on category.category_id = film_category.category_id
where name = 'Family';

select title as 'Title' from film
order by rental_duration desc;

select store.store_id as 'Store ID', sum(amount) as 'Total Business' from payment
left join staff on staff.staff_id = payment.staff_id
left join store on store.store_id = staff.store_id
group by store.store_id;

select store_id as 'Store ID', city.city as 'City', country.country as 'Country' from store
left join address on address.address_id = store.address_id
left join city on city.city_id = address.address_id
left join country on country.country_id = city.country_id;

select category.name as 'Genre', sum(amount) as 'Gross Revenue' from category
left join film_category on film_category.category_id = category.category_id
left join inventory on inventory.film_id = film_category.film_id
left join rental on rental.inventory_id = inventory.inventory_id
left join payment on payment.rental_id = rental.rental_id
group by Genre
order by `Gross Revenue` desc
limit 5;

create view Top_5_Categories_by_Gross_Revenue as
	select category.name as 'Genre', sum(amount) as 'Gross Revenue' from category
	left join film_category on film_category.category_id = category.category_id
	left join inventory on inventory.film_id = film_category.film_id
	left join rental on rental.inventory_id = inventory.inventory_id
	left join payment on payment.rental_id = rental.rental_id
	group by Genre
	order by `Gross Revenue` desc
	limit 5;

select * from Top_5_Categories_by_Gross_Revenue;

drop view if exists
Top_5_Categories_by_Gross_Revenue;