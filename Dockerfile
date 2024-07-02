# Use an official Python runtime as the parent image
FROM python:3.11-bullseye

RUN apt-get update && apt-get install -y \
    ffmpeg \
    imagemagick \
    ghostscript \
    fonts-roboto \
    cron \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Update font cache
RUN fc-cache -f -v

RUN sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container to /app
WORKDIR /app

# Install any Python packages specified in requirements.txt
# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Copy the local package directory content into the container at /app
COPY . /app

EXPOSE 31415

# Define any environment variables
# ENV KEY Value

# Print environment variables (for debugging purposes, you can remove this line if not needed)
RUN ["printenv"]

# Add cron job
RUN echo "0 */1 * * * /bin/bash /app/automate.sh" > /etc/cron.d/automate
RUN chmod 0644 /etc/cron.d/automate
RUN crontab /etc/cron.d/automate
RUN touch /var/log/cron.log
# Run Python script when the container launches
CMD cron && tail -f /var/log/cron.log


# To run ShortGPT docker:

#First make a .env file with the API keys like this:
#OPENAI_API_KEY=sk-_put_your_openai_api_key_here
#ELEVENLABS_API_KEY=put_your_eleven_labs_api_key_here
#PEXELS_API_KEY=put_your_pexels_api_key_here
#docker build -t short_gpt_docker:latest .
#docker run -p 31415:31415 --env-file .env short_gpt_docker:latest
#docker save short_gpt_docker > short_gpt_docker.tar
