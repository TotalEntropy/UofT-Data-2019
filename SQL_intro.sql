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
    
-- 2d --

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
    
-- Part 5 --

-- Part 6 --

select staff.first_name, staff.last_name
	from staff
    inner join address on staff.address_id = address.address_id;
    
select staff.first_name, staff.last_name, sum(payment.amount) as `Total Amount`
	from staff
    inner join payment on staff.staff_id = payment.staff_id
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
select title, language_id from film
	where title like ('K%') or title like ('Q%')
    ;