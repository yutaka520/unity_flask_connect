FROM nvidia/cuda:10.1-base
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
USER root

RUN apt-get update && \
    apt-get -y install locales && \
    apt-get -y install python3.6 python3-pip && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get install -y vim less && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install requests tqdm sentencepiece regex && \
    apt install -y wget && \
    pip3 install jaconv && \
    pip3 install hydra-core && \
    apt install net-tools && \
    pip3 install flask && \
    pip3 install flask_socketio && \
    pip3 install flask_cors && \
    pip3 install waitress