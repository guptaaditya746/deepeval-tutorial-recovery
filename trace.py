import asyncio

from deepeval.dataset import EvaluationDataset, Golden
from deepeval.tracing import observe, update_current_span, update_current_trace
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric


# 1. Dataset: examples we want to test.
dataset = EvaluationDataset(
    goldens=[
        Golden(input="Why is the sky blue?")
    ]
)


# 2. Top-level app.
# This becomes the full trace.
@observe()
async def my_ai_agent(query: str) -> str:
    chunks = await retrieve(query)
    answer = await generate(query, chunks)

    # This records the full app input and final output.
    update_current_trace(
        input=query,
        output=answer,
    )

    return answer


# 3. Internal component.
# This becomes one span inside the trace.
@observe()
async def retrieve(query: str) -> list[str]:
    return [
        "Sunlight contains many colors.",
        "Blue light is scattered more than red light by molecules in the atmosphere.",
    ]


# 4. Internal component we want to grade.
# The metric is attached here, so this span gets evaluated.
@observe(metrics=[AnswerRelevancyMetric()])
async def generate(query: str, chunks: list[str]) -> str:
    response = (
        "The sky looks blue because molecules in Earth's atmosphere scatter "
        "shorter blue wavelengths of sunlight more than longer red wavelengths."
    )

    # This creates the test case for the generate() span.
    update_current_span(
        test_case=LLMTestCase(
            input=query,
            actual_output=response,
            retrieval_context=chunks,
        ),
    )

    return response


# 5. Run each dataset example and evaluate the traces.
for golden in dataset.evals_iterator():
    task = asyncio.create_task(my_ai_agent(golden.input))
    dataset.evaluate(task)
