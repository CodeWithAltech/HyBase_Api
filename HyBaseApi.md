# HyBase API Documentation

## Overview

The HyBase API is a FastAPI-based backend service for managing events and users at Victoria University Kampala. This API provides endpoints for creating, reading, updating, and deleting events and user information.

## Base URL

The base URL for all API endpoints is: `https://hybase-api-vercel.app/api`

## Authentication

Currently, the API does not require authentication. This may change in future versions.

## Endpoints

### Events

#### Get all events

- **URL**: `/events/`
- **Method**: GET
- **Description**: Retrieves a list of all events.
- **Response**: Array of event objects

#### Get a specific event

- **URL**: `/post/{post_id}`
- **Method**: GET
- **Description**: Retrieves details of a specific event.
- **Parameters**: 
  - `post_id` (path parameter): The ID of the event
- **Response**: Event object

#### Create a new event

- **URL**: `/events/`
- **Method**: POST
- **Description**: Creates a new event.
- **Request Body**: EventBase object
- **Response**: Created event object

#### Update an event

- **URL**: `/post/{post_id}`
- **Method**: PUT
- **Description**: Updates an existing event.
- **Parameters**: 
  - `post_id` (path parameter): The ID of the event to update
- **Request Body**: EventBase object
- **Response**: Success message

#### Delete an event

- **URL**: `/post/{post_id}`
- **Method**: DELETE
- **Description**: Deletes a specific event.
- **Parameters**: 
  - `post_id` (path parameter): The ID of the event to delete
- **Response**: Success message

### Users

#### Get all users

- **URL**: `/users/`
- **Method**: GET
- **Description**: Retrieves a list of all users.
- **Response**: Array of user objects

#### Get a specific user

- **URL**: `/users/{user_id}`
- **Method**: GET
- **Description**: Retrieves details of a specific user.
- **Parameters**: 
  - `user_id` (path parameter): The ID of the user
- **Response**: User object

#### Create a new user

- **URL**: `/users/`
- **Method**: POST
- **Description**: Creates a new user.
- **Request Body**: UserBase object
- **Response**: Created user object

#### Update a user

- **URL**: `/users/{user_id}`
- **Method**: PUT
- **Description**: Updates an existing user.
- **Parameters**: 
  - `user_id` (path parameter): The ID of the user to update
- **Request Body**: UserBase object
- **Response**: Success message

#### Delete a user

- **URL**: `/users/{user_id}`
- **Method**: DELETE
- **Description**: Deletes a specific user.
- **Parameters**: 
  - `user_id` (path parameter): The ID of the user to delete
- **Response**: Success message

## Data Models

### EventBase

- `title`: string
- `description`: string
- `date`: string (format: "YYYY-MM-DD")
- `location`: string
- `category`: string
- `media`: string (URL to media file)

### UserBase

- `user_id`: UUID (optional, auto-generated if not provided)
- `name`: string
- `email`: string
- `telephone`: string (optional)

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests. In case of errors, a JSON object with an error message will be returned.

## Rate Limiting

Currently, there are no rate limits imposed on the API. This may change in future versions.

## Versioning

This documentation is for version 1.0 of the HyBase API. Future updates may introduce changes to the endpoints or data models.

## Support

For any issues or questions regarding the API, please contact the Victoria University IT department.

Made by Code With Altech

