FROM node
ADD .  /react_fastapi
WORKDIR /react_fastapi
RUN yarn install
RUN chmod -R 777 /react_fastapi
EXPOSE 3000
CMD ["npm","start"]