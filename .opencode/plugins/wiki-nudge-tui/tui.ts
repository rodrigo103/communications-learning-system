import { Plugin } from "@opencode/plugin/tui"

const NUDGE =
  "Evaluar si esta sesión generó conocimiento que deba compilarse al wiki de Sistemas de Comunicaciones. Derivaciones, resoluciones o estrategias de examen van al wiki."

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
        duration: 8000,
      })
    })
    return () => stop()
  },
})
