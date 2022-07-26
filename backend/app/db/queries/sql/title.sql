-- name: get-all-titles
SELECT title
FROM titles;


-- name: create-new-titles*!
INSERT INTO titles (title)
VALUES (:title)
ON CONFLICT DO NOTHING;
