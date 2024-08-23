# Use the official Bun image
FROM oven/bun:latest

# Set the working directory
WORKDIR /app

# Copy the package files
COPY package*.json ./

# Install dependencies using Bun
RUN bun install

# Copy the rest of the application code
COPY . .

# Build the application
RUN bun run build

# Command to run the development server
CMD ["bun", "run", "dev"]
