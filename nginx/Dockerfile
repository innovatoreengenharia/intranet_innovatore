FROM nginx:1.25

# RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d

ENV HOME=/usr/src/app
RUN mkdir -p $HOME
ENV APP_HOME=/usr/src/app
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/static
RUN mkdir -p $APP_HOME/media
WORKDIR $APP_HOME