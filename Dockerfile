FROM centos:centos8
 
WORKDIR /work
 
RUN dnf -y update \
 && dnf group install -y "Development Tools" \
 && dnf install -y openssh-server \
    openssh-clients \
    mysql \
    mysql-devel \
    httpd \
    httpd-tools \
    httpd-devel \
    python38 \
    python38-devel \
    python38-mod_wsgi \
    langpacks-ja \
 && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
 && dnf clean all
 
ENV TZ="Asia/Tokyo" \
    LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
 
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
 
# SSH設定
# rootでのログインを許可
# ポートを22から20022に変更
# rootのパスワードをpasswordに設定
# ssh-keygenでホスト鍵を作成しておかないとSSHの起動に失敗する
RUN /usr/bin/ssh-keygen -A \
 && sed -ri 's/^#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed -ri 's/^#Port 22/Port 20022/' /etc/ssh/sshd_config \
 && echo 'root:password' | chpasswd
 
EXPOSE 80
EXPOSE 20022
 
# SSHとApacheを起動
CMD ["sh","-c","/usr/sbin/sshd && /usr/sbin/httpd -D FOREGROUND"]