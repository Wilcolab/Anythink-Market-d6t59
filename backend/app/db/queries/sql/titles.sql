-- name: get-all-tags
SELECT title
FROM titles;


-- name: create-new-tags*!
INSERT INTO titles (title)
VALUES (:title)
ON CONFLICT DO NOTHING;
