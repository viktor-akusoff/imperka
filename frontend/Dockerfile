FROM node:lts-slim as build-stage

ARG API_URL

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .
RUN echo "NUXT_PUBLIC_API_URL=${API_URL}" > ./.env
RUN npm install && npm run build

FROM node:lts-slim as run-stage

COPY --from=build-stage /usr/src/app/.output .output

EXPOSE 3000

ENTRYPOINT ["node", "./.output/server/index.mjs"]