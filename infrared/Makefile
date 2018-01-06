all:

run:	lirc_run docker_run

docker_image:
	(cd cec-mqtt-bridge; docker image build --tag mqtt-bridge .)

docker_run:
	docker run -d --rm --net=host -v /var/run/lirc:/var/run/lirc \
                           --name mqtt-bridge mqtt-bridge

docker_logs:
	docker logs -f --tail 20 mqtt-bridge

lirc_run:
	lircd /storage/infrared/etc/lircd.conf

