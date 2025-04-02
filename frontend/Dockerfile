FROM node:20-alpine

WORKDIR /app

# Copy package files and install dependencies
# Copy package*.json first to leverage Docker cache
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose the Vite dev server port
EXPOSE 5173

# Default command to run the Vite dev server
# Use --host to allow connections from outside the container
CMD ["npm", "run", "dev", "--", "--host"]
