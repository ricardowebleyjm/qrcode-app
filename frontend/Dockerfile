FROM node:latest

# Set working directory in the container
WORKDIR /app

# Copy all files from the frontend directory to the container
COPY . /app/


# Install dependencies
RUN npm install

RUN npm run build

# Expose port 80
EXPOSE 80

# Start the app
CMD ["npm", "run", "dev"]
