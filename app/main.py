import uuid
import os

import httpx
from dispike import Dispike
from dispike.register.models import DiscordCommand
from dispike.models import IncomingDiscordInteraction
from dispike.response import DiscordResponse

# Do some monkey patching to listen on host "0.0.0.0". Otherwise, calls won't be 
# forwarded to our server.
class DispikePatched(Dispike):
    def run(self, port: int = 5000):

        """Runs the bot with the already-installed Uvicorn webserver.

        Args:
            port (int, optional): Port to run the bot over. Defaults to 5000.
        """

        uvicorn = self._return_uvicorn_run_function()
        uvicorn.run(app=self.referenced_application, host="0.0.0.0", port=port)

bot = DispikePatched(client_public_key="79adb8106238dcddfd3a228b8587bf20a86ae9f25fa809f7269e278eca9412b5",
                     bot_token="ODM2NTM2MjQ0NzYyNDQzNzk2.YIfbFg.mY-0y-wo3bfJqQWDFDMqPTnULC0",
                     application_id="836536244762443796")


cmd = DiscordCommand(
    name="secret", description="Discover the secret of this channel.", options=[]
)
bot.register(cmd)



@bot.interaction.on("secret")
async def handle_secret(*args, **kwargs) -> DiscordResponse:
    resp = DiscordResponse(
            # yields channel message type 4
            show_user_input=True,
            content=f"""
            Hello, hello, hello - welcome to our channel!
            My name is CocoBot. Im running on SAP Cloud Platform.
            """,
            empherical=True,
        )
    return resp


@bot.interaction.on("forex.latest.convert")
async def handle_forex_conversion_rates(
    symbol_1: str, symbol_2: str, ctx: IncomingDiscordInteraction
) -> DiscordResponse:
    async with httpx.AsyncClient() as client:
        try:
            _send_request = await client.get(
                f"https://api.ratesapi.io/api/latest?base={symbol_1.upper()}&symbols={symbol_2.upper()}"
            )
            if _send_request.status_code == 400:
                return DiscordResponse(
                    content=f"Unable to find that forex due to an error: {_send_request.json()['error']}"
                )
            elif _send_request.status_code == 200:
                _parse_request = _send_request.json()
                return DiscordResponse(
                    content=f"1 {symbol_1.upper()} ~= {_parse_request['rates'][symbol_2.upper()]} {symbol_2.upper()}",
                    show_user_input=True,
                )
            else:
                return DiscordResponse(
                    content=f"There was an issue contacting the Forex API. {_send_request.status_code}",
                    empherical=True,
                )
        except Exception:
            return DiscordResponse(
                content="There was an issue with our bot. Try again later."
            )


if __name__ == "__main__":
    if os.environ['DEV'] == 'True':
        port = int(os.environ['PORT'])
        bot.run(port)
