# Imperka CMS - Simple and Flexible Content Management System

[2024-07-31 00-34-54.webm](https://github.com/user-attachments/assets/49986d6a-ca3f-42ee-a2fe-ee3166a64f08)

Imperka CMS is a self-hosted content management system (CMS) built for simplicity, flexibility, and ease of use. It's designed to empower you to create and manage beautiful websites with complete control over content and design. 

This project leverages a modern tech stack, including FastAPI for the backend, Nuxt.js for the frontend, and MongoDB for the database, ensuring high performance, scalability, and security.


## Key Features

- **Intuitive Page Editor:** 
    - UI fully ready for easy content arrangement.
    - Real-time preview of changes.
    - WYSIWYG editor for text formatting. 
- **Versatile Content Blocks:**
    - **Text:** Format text with headings, lists, links, and more.
    - **Images:** Upload, display, and manage images in various sizes and formats. Create galleries and slideshows.
    - **Video:** Embed videos from YouTube and other platforms.
    - **HTML:**  Embed custom HTML code for widgets, scripts, and interactive elements.
    - **Recommendations:** Automatically display links to related pages using hashtags for content discovery.
- **Media Management System:**
    - Easily upload, store, and manage images and videos for use on your pages.
- **Modern Technology Stack:**
    - FastAPI (Python) for a high-performance and efficient backend API.
    - Nuxt.js (Vue.js) for a versatile and SEO-friendly frontend with server-side rendering (SSR).
    - MongoDB for a flexible and scalable NoSQL database.
    - Docker Compose for easy deployment and management. 

## Benefits

- **Total Control:** You own your website and have complete control over its content, design, and functionality. No limitations from third-party platforms.
- **Easy Customization and Extensibility:** Adapt Imperka CMS to your unique needs by creating custom templates, blocks, modules, and integrations. 
- **High Performance and Security:**  Built with a focus on speed, efficiency, and security best practices. 
- **Open Source:** Explore the code, contribute improvements, or tailor it to your specific requirements.
- **Continuous Development:**  Imperka CMS is actively maintained and enhanced with new features. 

## How It Works

- **Modular Architecture:** Imperka CMS is divided into independent modules for various functionalities (pages, media, authentication, etc.), allowing for easy extensibility.
- **API-First Approach:**  The frontend and backend communicate through a RESTful API, providing flexibility and making it easy to integrate with other systems or create custom clients. 

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/viktor-akusoff/imperka.git 
   ```

2. **Navigate to the project directory:**
   ```bash
   cd imperka
   ```

3. **Create the following files and populate them with your desired values:**
    - `backend/app/secret_key`:  Secret key for JWT authentication
    - `backend/app/username`:  Admin username 
    - `backend/app/password`:  Admin password (plain text, it will be hashed on first startup) 

### Running in Production

1. **Build and start the containers:**
    ```bash
    docker compose up -d 
    ```

### Running in Development Mode (with hot reload)

1. **Build and start the containers using the development Docker Compose file:**
    ```bash
    docker compose -f docker-compose.dev.yml up --watch
    ```

## Usage

1. **Access the admin panel:**
    - After starting the containers, the admin panel will be available at: [http://localhost:3000/login](http://localhost:3000/login). 
    - Log in using the admin username and password you created during installation.
2. **Create pages:**
    - Use the intuitive page editor to add and arrange content blocks.
3. **Upload media:**
    - Manage your images and videos in the media library.

## Contributing

Contributions are welcome!  Feel free to open issues, submit pull requests, or share your ideas for improvements. 

## License

This project is licensed under the MIT License.
