# RESTful API Fundamentals: HTTP, curl, and Security

This document summarizes the key concepts covered in Tasks 0 and 1 of the RESTful API project.

---

# Task 0: Basics of HTTP/HTTPS

## Difference Between HTTP and HTTPS

- **HTTP** (HyperText Transfer Protocol) is the protocol used for communication between a client (browser) and a web server.
- **HTTPS** (HTTP Secure) is the secure version of HTTP. It uses SSL/TLS encryption to secure data during transmission.

### Key Differences

| HTTP                       | HTTPS                            |
| -------------------------- | -------------------------------- |
| No encryption              | Encrypted communication          |
| Uses port 80               | Uses port 443                    |
| Vulnerable to interception | Protected against eavesdropping  |
| No identity verification   | Certificate-based authentication |

HTTPS ensures:

- **Confidentiality** — data cannot be read by third parties
- **Integrity** — data cannot be tampered with
- **Authentication** — the server's identity is verified

---

## Structure of an HTTP Request

An HTTP request contains:

### Request Line

```
GET /posts HTTP/1.1
```

- Method (GET, POST, etc.)
- Path
- HTTP version

### Headers

- `Host`
- `User-Agent`
- `Accept`
- `Authorization`
- `Content-Type`

### Optional Body

Used with POST, PUT, or PATCH to send data.

---

## Structure of an HTTP Response

### Status Line

```
HTTP/1.1 200 OK
```

### Headers

- `Content-Type`
- `Content-Length`
- `Server`
- `Cache-Control`

### Body

Contains HTML, JSON, or other data.

---

## Common HTTP Methods

| Method | Description      | Use Case                              |
| ------ | ---------------- | ------------------------------------- |
| GET    | Retrieve data    | Fetch a webpage or API data           |
| POST   | Send data        | Create a new resource                 |
| PUT    | Update resource  | Replace an existing resource entirely |
| PATCH  | Partially update | Modify specific fields of a resource  |
| DELETE | Remove resource  | Delete a resource                     |

---

## Common HTTP Status Codes

| Code | Meaning               | Scenario                             |
| ---- | --------------------- | ------------------------------------ |
| 200  | OK                    | Successful request                   |
| 201  | Created               | Resource successfully created        |
| 400  | Bad Request           | Invalid input sent by the client     |
| 401  | Unauthorized          | Authentication failed                |
| 404  | Not Found             | Resource doesn't exist on the server |
| 500  | Internal Server Error | Server-side failure                  |

---

# Task 1: Consuming an API with curl

## Checking curl Installation

```bash
curl --version
```

Displays the installed version of curl and its supported protocols.

---

## Fetching a Webpage

```bash
curl http://example.com
```

Sends a GET request and returns the HTML content of the page.

---

## Fetching API Data

```bash
curl https://jsonplaceholder.typicode.com/posts
```

Returns a JSON array of posts, each containing:

- `userId`
- `id`
- `title`
- `body`

---

## Fetching Only Headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

The `-I` flag retrieves only the response headers (without the body).

Useful for:

- Checking status codes
- Inspecting content type
- Debugging server configuration

---

## Making a POST Request

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

- `-X POST` specifies the HTTP method
- `-d` sends the request body data

The API responds with a simulated created resource, returning the new post with an `id` of `101` (JSONPlaceholder simulates creation without actually saving the data).

---

## Conclusion

Through these tasks, we learned:

- The difference between HTTP and HTTPS
- How HTTP requests and responses are structured
- The purpose of common HTTP methods and status codes
- How to interact with APIs using curl
- How client-server communication works in practice

These fundamentals are essential for understanding RESTful APIs and web development.
