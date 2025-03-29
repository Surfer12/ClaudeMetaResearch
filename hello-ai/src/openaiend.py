import MistralAI from "mistralai";

const apiKey = "my api key"; // defaults to process.env["MISTRAL_API_KEY"]
const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${1f4579cda5f6fb7a3a15ac6438ae7da3}/${mystery}/mistral`;


const mistralai = new MistralAI({
  apiKey,
  baseURL,
});

try {
  const model = "Mistral Small 25.02";
  const messages = [{ role: "user", content: "What is a neuron?" }];
  const maxTokens = 100;

  const chatCompletion = await mistralai.chat.completions.create({
    model,
    messages,
    max_tokens: maxTokens,
  });

  const response = chatCompletion.choices[0].message;

  return new Response(JSON.stringify(response));
} catch (e) {
  return new Response(e);
}
export default {
  async fetch(request, env, ctx): Promise<Response> {
    const mistralai = new MistralAI({
      apiKey: env.MISTRAL_API_KEY,
    });

    // Create a TransformStream to handle streaming data
    let { readable, writable } = new TransformStream();
    let writer = writable.getWriter();
    const textEncoder = new TextEncoder();

    ctx.waitUntil(
      (async () => {
        const stream = await mistralai.chat.completions.create({
          model: "Mistral Small 25.02",
          messages: [{ role: "user", content: "Tell me a story" }],
          stream: true,
        });

        // loop over the data as it is streamed and write to the writeable
        for await (const part of stream) {
          writer.write(
            textEncoder.encode(part.choices[0]?.delta?.content || ""),
          );
        }
        writer.close();
      })(),
    );

    // Send the readable back to the browser
    return new Response(readable);
  },
} satisfies ExportedHandler<Env>;


