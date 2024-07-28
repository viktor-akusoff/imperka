import axios from 'axios'
import { onMounted } from 'vue'

const ACCESS_TOKEN_KEY = 'access_token'
const REFRESH_TOKEN_KEY = 'refresh_token'

export default function () {
    const config = useRuntimeConfig()

    const accessToken = ref(null);
    const refreshToken = ref(null);

    onMounted(() => {
        accessToken.value = localStorage.getItem(ACCESS_TOKEN_KEY) || null;
        refreshToken.value = localStorage.getItem(REFRESH_TOKEN_KEY) || null;    
    })

    const isAuthenticated = computed(() => !!accessToken.value);

    const setTokens = (newAccessToken, newRefreshToken) => {
        accessToken.value = newAccessToken;
        refreshToken.value = newRefreshToken;

        localStorage.setItem(ACCESS_TOKEN_KEY, newAccessToken);
        localStorage.setItem(REFRESH_TOKEN_KEY, newRefreshToken);
    };

    const clearTokens = () => {
        accessToken.value = null;
        refreshToken.value = null;

        localStorage.removeItem(ACCESS_TOKEN_KEY);
        localStorage.removeItem(REFRESH_TOKEN_KEY);
    };

    const apiClient = axios.create({
        baseURL: config.public.apiUrl
    });

    apiClient.interceptors.request.use(
        (config) => {
            config.headers.Authorization = `Bearer ${localStorage.getItem('access_token')}`;
            return config; 
        },
        (error) => {
            return Promise.reject(error);
        }
    );

    apiClient.interceptors.response.use(
        (response) => {
            return response;
        },
        async (error) => {
            const originalRequest = error.config;
            if (
                error.response.status === 401 && 
                !originalRequest._retry &&
                refreshToken.value
            ) {
                originalRequest._retry = true; 
                try {
                    const response = await apiClient.post('/auth/refresh', {
                        refresh_token: refreshToken.value 
                    });

                    const { access_token: newAccessToken } = response.data;
                    setTokens(newAccessToken, refreshToken.value);

                    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                    return apiClient(originalRequest);
                } catch (refreshError) {
                    clearTokens(); 
                    return Promise.reject(refreshError); 
                }
            }
            return Promise.reject(error);
        }
    );

    return {
        accessToken,
        refreshToken,
        isAuthenticated,
        setTokens,
        clearTokens,
        apiClient
    };
}