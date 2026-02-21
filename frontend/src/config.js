const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export const API_ENDPOINTS = {
    CATEGORIES: `${API_URL}/api/v1/categories`,
    PRODUCTS: `${API_URL}/api/v1/products`,
    CUSTOMERS: `${API_URL}/api/v1/customers`,
    TRANSACTIONS: `${API_URL}/api/v1/transactions`,
    AUTH: {
        LOGIN: `${API_URL}/api/v1/auth/login`,
        SIGNUP: `${API_URL}/api/v1/auth/signup`,
    },
    DASHBOARD: `${API_URL}/api/v1/dashboard`, // Assuming there's a dashboard endpoint
    REPORTS: `${API_URL}/api/v1/reports`,
};

export default API_URL;
