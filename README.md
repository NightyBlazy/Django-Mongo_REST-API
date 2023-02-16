# TsunblogAPI-Django_Mongo

A alternative REST API for my [Tsunblog](https://github.com/NightyBlazy/TsunBlog "My Tsunblog Project") project

## How to use:

1. Create an Python virtual environment
2. Install required libraries with `pip install requirements.txt` command inside root directory
3. Create an `.env` file inside root directory and add `MONGO_DBNAME`, `MONGO_HOST`, `MONGO_PORT`, `SECRET_KEY` fields inside that file
4. Fill `MONGO` fields with your informations about your MongoDB. You can put whatever you want in `SECRET_KEY` field. But make sure to make it unpredictable.
5. And lastly, to run the server, run `python -u manage.py runserver` command inside `demongo` directory

## Notes:

To use this API with [Tsunblog](https://github.com/NightyBlazy/TsunBlog "My Tsunblog Project") project, you have make a little bit change in that project

1. In `Blogs.tsx`, change `post._id` variables to `post.id`
2. In `Create.tsx`, add `/` at the end of the fetch URL
