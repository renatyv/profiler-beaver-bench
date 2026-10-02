/**
 * turn_guard — hard agent turn-cap for the containerized BEAVER runner.
 *
 * This extension owns the hard lifecycle cap. After the penultimate turn it
 * removes tools and tells the model to use its final turn for SQL, then aborts
 * if that response contains no SQL.
 *
 * It registers NO tools and reads NO MySQL credentials — pure lifecycle guard.
 *
 * Env:
 *   BEAVER_MAX_TURNS   agent turn cap (default 10). Last turn is answer-only.
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const MAX_TURNS = Number(process.env.BEAVER_MAX_TURNS ?? "10");
const FINAL_SQL = /(?:<ans>|```(?:sql|mysql)?\s*\n)\s*(?:SELECT|WITH|\()/i;

export default function turnGuardExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (event, ctx) => {
    turnCount += 1;
    if (turnCount === MAX_TURNS - 1 && event.message.stopReason === "toolUse") {
      pi.setActiveTools([]);
      pi.sendMessage({
        customType: "turn-guard",
        content: "FINAL TURN: Tools are now disabled. Return your best complete MySQL query immediately inside <ans>...</ans>. Do not explain.",
        display: false,
      }, { deliverAs: "steer" });
      return;
    }
    if (turnCount === MAX_TURNS) {
      const text = Array.isArray(event.message.content)
        ? event.message.content.filter((part) => part.type === "text").map((part) => part.text).join("")
        : "";
      if (!FINAL_SQL.test(text)) {
        pi.setActiveTools([]);
        try { ctx.abort(); } catch { /* ignore */ }
      }
      return;
    }
    if (turnCount > MAX_TURNS) {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });
}
