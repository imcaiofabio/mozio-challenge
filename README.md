
The API domain URL was sent via email.

## API Endpoints

### Docs
- `GET /docs`: Swagger UI listing all endpoints to be tested
- `GET /docs-view`: ReDoc UI for API documentation

### Providers

- `GET /providers/`: Get a list of all providers.
- `POST /providers/`: Create a new provider.
- `GET /providers/{id}/`: Get details of a specific provider.
- `PUT /providers/{id}/`: Update details of a specific provider.
- `DELETE /providers/{id}/`: Delete a specific provider.

### Service Areas

- `GET /service-areas/`: Get a list of all service areas.
- `POST /service-areas/`: Create a new service area.
- `GET /service-areas/{id}/`: Get details of a specific service area.
- `PUT /service-areas/{id}/`: Update details of a specific service area.
- `DELETE /service-areas/{id}/`: Delete a specific service area.

### Polygon Lookup

- `GET /polygons/?lat={latitude}&lng={longitude}`: Get a list of polygons that include the given latitude and longitude pair. The name of the polygon, provider's name, and price are returned for each polygon.
