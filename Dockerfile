FROM centos:latest
MAINTAINER bmahajan0@gmail.com

RUN yum -y install wget* java-1.8.0*

WORKDIR /opt

RUN wget http://apache.cs.utah.edu/tomcat/tomcat-9/v9.0.24/bin/apache-tomcat-9.0.24.tar.gz


ADD http://mirrors.jenkins.io/war-stable/latest/jenkins.war /opt/apache-tomcat-9.0.24/webapps/

RUN tar -xzvf /opt/apache-tomcat-9.0.24.tar.gz

EXPOSE 8080

ENTRYPOINT ["/opt/apache-tomcat-9.0.24/bin/catalina.sh", "run"]
 
##
