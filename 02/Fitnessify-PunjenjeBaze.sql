INSERT INTO account VALUES (0, 'username', 'user.username@email.com', '2c2bf00079a6d49a8f7fb17cefb52fdb41a4b043', 'user');
INSERT INTO account VALUES (1, 'marta', 'marta.marta@email.com', 'aaaaf00079a6d49a8f7fb17cefb52fdb41a4aaaa', 'user');
INSERT INTO account VALUES (2, 'dora', 'dora.dora@email.com', 'bbbbf00079a6d49a8f7fb17cefb52fdb41a4bbbb', 'user');

INSERT INTO goals VALUES (0, 0, 100, 60, 1000, NULL);
INSERT INTO goals VALUES (1, 1, NULL, 30, 6000, 60.5);
INSERT INTO goals VALUES (2, 2, NULL, NULL, 1000, 55.3);

INSERT INTO exercise VALUES (0, 'squats', 'lorem ipsum', 100);
INSERT INTO exercise VALUES (1, 'lunges', 'The lunge is a popular leg-strengthening exercise with a multitude of variations to add variety to your workout. In addition, varying your technique allows you to emphasize different muscles or parts of those muscles.', NULL);
INSERT INTO exercise VALUES (2, 'push ups', 'lorem ipsum lorem ipsum', 50);

INSERT INTO account_exercise (account_id, exercise_id, date_of_exercise) VALUES (1, 0, Now());
INSERT INTO account_exercise (account_id, exercise_id, date_of_exercise) VALUES (1, 1, Now());
INSERT INTO account_exercise (account_id, exercise_id, date_of_exercise) VALUES (2, 2, Now());

INSERT INTO ingredient (name, calories, nutrients) VALUES ('egg', 78, 'Total Fat: 4.8g, Protein: 6.3g');
INSERT INTO ingredient (name, calories, nutrients) VALUES ('carrot', 16, NULL);
INSERT INTO ingredient (name, calories, nutrients) VALUES ('white bread', 98, 'Total Fat: 1.2g, Protein: 3.3g');

INSERT INTO account_ingredient VALUES (1, 1, Now());
INSERT INTO account_ingredient VALUES (2, 3, Now());
INSERT INTO account_ingredient VALUES (2, 2, Now());

INSERT INTO recipe VALUES (0, 'Lasagne', 'Bring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes. Drain noodles, and rinse with cold water. In a mixing bowl, combine ricotta cheese with egg, remaining parsley, and 1/2 teaspoon salt.', 448, 'protein:29.7g, fat 21.3g', 180);
INSERT INTO recipe VALUES (1, 'Pancakes', 'lorem ipsum', 234, 'fat 8.2g, protein 6.4g', 30);
INSERT INTO recipe VALUES (2, 'Tacos', 'Season beef with onion powder, garlic salt, celery salt, and cumin. Pour tomato sauce over the beef, stir to coat, and simmer until thickened, slightly, about 5 minutes.', 188, NULL, 15);

INSERT INTO account_recipe VALUES (0, 0);
INSERT INTO account_recipe VALUES (1, 1);
INSERT INTO account_recipe VALUES (2, 2);

INSERT INTO ingredient_recipe VALUES (2, 0, 3);
INSERT INTO ingredient_recipe VALUES (2, 2, 2);
INSERT INTO ingredient_recipe VALUES (1, 2, 4);
