from gevent import monkey
monkey.patch_all()

from ssi_fctrading import FCTradingStream, fc_stream
from ssi_fctrading import FCTradingClient
from . import fc_config


def on_message(tapi_message):
	print("fc_received: " + tapi_message)


def on_error(tapi_error):
	print("fc_error: " + tapi_error)


def tapi_data_streaming(on_message, on_error):
	client = FCTradingClient(fc_config.Url, fc_config.ConsumerID,
	fc_config.ConsumerSecret, fc_config.PrivateKey, fc_config.TwoFAType)
	print("access_token: "+ client.get_access_token())
	stream_client = FCTradingStream(client, fc_config.StreamURL, on_message, on_error, "0")
	stream_client.start()


# main function
if __name__ == '__main__':
	from gevent import monkey
	monkey.patch_all()
	tapi_data_streaming(on_message, on_error)