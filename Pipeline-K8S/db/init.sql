-- Drop the database if it exists
DROP DATABASE IF EXISTS devopsroles;

-- Create the database
CREATE DATABASE devopsroles;

-- Use the database
USE devopsroles;

-- Create the table
CREATE TABLE test_table (
  url VARCHAR(200)
);

-- Insert data into the table
INSERT INTO test_table(url)
VALUES
  ('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXkwempocWhwbHd0MnRreWk1azgwN2VsMHVoZ2NzM3FhODFzc2M2NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7527pa7qs9kCG78A/giphy.gifJ'),
  ('https://media1.giphy.com/media/RQSuZfuylVNAY/200w.webp?cid=ecf05e47n4cdqaz5msne59cx3fvz6c5y9sg13y19tehfwwck&ep=v1_gifs_search&rid=200w.webp&ct=g'),
  ('https://media4.giphy.com/media/1LweXxLwVT0J2/giphy.webp?cid=ecf05e47i5esvlro7tjmr4y9uo7wk5ewduom4h8qmqzfb7cr&ep=v1_gifs_search&rid=giphy.webp&ct=g'),
  ('https://media0.giphy.com/media/BpDYodBlBXFIs/200.webp?cid=ecf05e4720mh0y949f7ue74r5xst5lnjcabxz4njc81al1nz&ep=v1_gifs_search&rid=200.webp&ct=g'),
  ('https://media4.giphy.com/media/a5MdgE5zfNZrW/giphy.webp?cid=ecf05e47c8yxnbizuxbowo5eu3cllut9jxq7f7e7hyz69omv&ep=v1_gifs_search&rid=giphy.webp&ct=g'),
  ('https://media0.giphy.com/media/bhSi84uFsp66s/200.webp?cid=ecf05e47bek95fdlgsjvp4y0ckd9op99cwli90zt1olliwwf&ep=v1_gifs_search&rid=200.webp&ct=g'),
  ('https://media3.giphy.com/media/x9q0Y6F0BGoTBoqxuV/giphy.webp?cid=ecf05e47rpgbqex2pq000crgh2m76g5jxrqhko46tos5nyvl&ep=v1_gifs_search&rid=giphy.webp&ct=g'),
  ('https://media0.giphy.com/media/Ssq1XEzD0D6SI/giphy.webp?cid=ecf05e474etxjps0ok99zsj263u0aq6f8ymogvqwou0l5wsr&ep=v1_gifs_search&rid=giphy.webp&ct=g');
