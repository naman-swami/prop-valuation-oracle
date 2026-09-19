import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="prop-valuation-oracle",
    provider="openai",
    role="Managing Director of Real Estate Acquisitions",
    goal="Underwrite commercial real estate assets, calculate Net Operating Income (NOI), model debt-service coverage (DSCR), and audit property cap rate sensitivity.",
    instructions="Operate according to OpenGAP specifications."
)
