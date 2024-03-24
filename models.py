import typing as t

from _types import Message, Parameters, Role
from openai import AsyncOpenAI

from openai.types.chat import ChatCompletionMessageParam


async def _chat_openai(
    client: AsyncOpenAI, messages: t.List[Message], parameters: Parameters
) -> Message:
    response = await client.chat.completions.create(
        model=parameters.model,
        messages=t.cast(t.List[ChatCompletionMessageParam], messages),
        temperature=parameters.temperature,
        max_tokens=parameters.max_tokens,
        top_p=parameters.top_p,
    )

    response_message = response.choices[0].message
    return Message(
        role=Role(response_message.role), content=str(response_message.content)
    )


async def chat_openai(messages: t.List[Message], parameters: Parameters) -> Message:
    return await _chat_openai(AsyncOpenAI(), messages, parameters)

