import { Plugin } from "@opencode/plugin/tui"

const NUDGE =
  "Evaluar si esta sesión generó conocimiento para el wiki de Sistemas de Comunicaciones (wiki/). Procesos, explicaciones de conceptos, resoluciones o estrategias de examen van al wiki. Revisá la sección 'LLM Wiki' en AGENTS.md; si aplica, corré /wiki ingest."

export default Plugin.define({
  id: "wiki-nudge.tui",
  setup(context) {
    const here = context.location?.directory
    const stop = context.data.on("session.execution.succeeded", (event) => {
      if (Math.random() >= 0.33) return
      const sessionID = event.data.sessionID
      let dir: string | undefined = event.location?.directory
      if (!dir) {
        try {
          dir = context.data.session.get(sessionID)?.location?.directory
        } catch {}
      }
      if (here && dir && dir !== here) return
      context.ui.toast.show({
        title: "wiki-nudge",
        message: NUDGE,
        duration: 12000,
      })
    })
    return () => stop()
  },
})
