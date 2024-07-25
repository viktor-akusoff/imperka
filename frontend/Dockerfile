FROM node:lts-slim as build-stage

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .
RUN npm ci && npm run build

FROM node:lts-slim as run-stage

COPY --from=build-stage /usr/src/app/.output .output

EXPOSE 3000

ENTRYPOINT ["node", "./.output/server/index.mjs"]