# How Sub Agents Work in Claude Code

## Understanding Sub Agents

Claude introduced the sub agent feature a few weeks ago, and it was a super exciting concept. However, for people who tried it, they often got quite a negative experience where sub agents felt slow, consumed much more tokens, and most importantly, it didn't feel like they were contributing to better results. I was among one of those people, but only recently I started learning the best practices of using sub agents, and that has totally changed the game and made my Claude Code perform much better consistently. That's why today I want to share how I think about and design sub agent systems.

First, we need to understand why Claude Code introduced the sub agent concept initially. If you don't know how exactly Claude Code agent works behind the scenes, it's basically a tool-called agent that's equipped with a list of different tools to read files, list all files, edit files, and things like that. Some of these tools can consume a lot more tokens, like the read tool, because you're going to include the whole content of a file into the conversation history.

Before Claude Code had the sub agent feature, everything would be done by the Claude Code agent itself, which means before it started implementing, it might already use 80% of the context window because those files would contain large amounts of context. This would likely trigger the compact conversation command that would summarize the whole conversation before it could proceed. As we know, every time you compact conversation, the performance drops dramatically because it starts losing context about what it has done before.

That's why they later introduced the task tool for the Claude Code agent. It allows Claude Code to assign a task to another agent, and this agent will have the exact same set of tools, including read file and search file. So you can trigger this agent to actually scan the whole codebase, understand what are all the relevant files to change, and then based on that information, do the actual implementation.

The way this saves tokens is because from the parent agent's perspective, all the steps that the sub agent takes in the middle won't be part of the conversation history for the parent agent. It can only see that it assigned a task to the sub agent, and then the sub agent came back with a summary of the research report, which can be used to guide the next best action. By doing that, you effectively turn those massive token consumptions from read file and search file actions into something like just a few hundred token summary, but still containing the most important information to guide the next action.

## Why Implementation-Focused Sub Agents Don't Work

The whole purpose of sub agents has been around context engineering and context optimization. But where things fail is when people start trying to get sub agents to not only do the research work but also directly do the implementation.

For example, my first thought was: what if we can have a frontend dev agent to do just frontend implementation with special rules and workflows, as well as a backend dev agent who is specialized in backend implementation? Then for the parent agent, it would really just orchestrate the whole conversation and delegate tasks to others.

This sounds really good at the beginning, but the moment whatever the sub agent implemented is not 100% correct and you want the agent to fix it, that's where the problem begins. For each agent, it only has very limited information about what is going on. The frontend dev agent only knows the actions it took as well as the final message it generated in that specific task. Same for the backend dev agent.

If you prompt the Claude Code agent that there's a frontend bug, even though it's assigned to the frontend dev again, this will just trigger a new conversation because the frontend dev agent wouldn't know what happened before in the last frontend session and also won't have any context about what the backend dev has done before. Each task is a very contained session.

Meanwhile, for the parent Claude Code agent, it also has very limited information because again, it won't see all the actions that have been taken by the sub agent, which means it won't know what specific files have been created and what they actually put in those files. All the parent agent sees is: "I assigned task to frontend dev, and frontend dev came back saying I completed the task," and the same thing for the backend.

So if you want to get the Claude Code agent to fix the bug itself, it will have very limited information about what is causing the issue. This will probably be resolved later in the future when we figure out a good way to share context across those different agents so that each one of them is always on the same page about what has been done.

## The Right Way to Design Sub Agents

But for now, the best practice would be to consider each sub agent almost as a researcher and think about what kind of planning and research steps can actually dramatically improve your current AI coding workflow.

I also received similar feedback from Adam Wolf, who is one of the key engineers on the Claude Code team, where he says sub agents work best when they're just looking for information and providing a small amount of summary back to the main conversation thread.

With this insight, I got an idea: what if each service provider like Vercel AI SDK, Supabase, Tailwind could have one agent that is equipped with all the latest knowledge about their documentation, best practices, and design? Then this agent can start looking through my existing codebase to figure out an implementation plan.

This is exactly what I tried. I started creating different expert sub agents for each service. For example, a Shadcn agent that has access to a special MCP tool that can retrieve relevant components and design to do a really good frontend job, or a Vercel AI SDK expert that is loaded with the latest Vercel SDK v5 docs (because they just released this new version a couple weeks ago), or a Stripe expert that is loaded with the latest Stripe docs as well as tools like Context7 so you can do complex setups like usage-based pricing very easily.

## Context Management Through File System

Meanwhile, I also did some optimization about context sharing across different agents. This is something I learned from Manus team's blog on context engineering, where they talk about all the tricks and tips of how they make Manus execute long-running tasks. There's a lot of good stuff in there, but the part that inspired me most is how they use the file system as the ultimate context management system.

Instead of storing all the tool results in the conversation history directly, they save the result to a local file which can be retrieved later. In their case, when the agent runs a web scraping tool, instead of including the whole content scraped inside the conversation history directly (which might take more than 10,000 tokens), they will just save the scraped content into a local markdown file, which can be retrieved later at any point in the conversation.

This is exactly what I designed. Inside the `.doc/claude` folder, there will be a task folder that contains the context of each feature that you want the team to implement. Meanwhile, each sub agent can start creating those markdown files about the specific research report and implementation plan.

The process is: the parent agent will always create a context file that includes all the information about the specific project we're trying to execute. For every sub agent, before they start doing the work, they will read this context file first to understand the overall project plan and where things are at now. After they finish, they will also update the context file to indicate what the core steps they did were and save the research report into a markdown file in the docs. So the parent agent or all the other agents can just read this doc later for getting more context.

This setup has dramatically improved the success rate and results for my Claude Code.

## Building Specialized Sub Agents

To build those sub agents, the general rule I have is that I will include a lot of important docs directly inside the system prompt so I can have confidence that it will follow the latest practices. Meanwhile, I will also give them relevant tools to retrieve important context.

In the Shadcn expert example, there's an MCP tool specifically designed for information retrieval from that specific package. One is the Shadcn component MCP - it allows you to retrieve components, the example code for each component, and relevant blocks. Another MCP tool retrieves themes for Shadcn, from a website called Twinx which is specialized in theme design.

For the agent setup, I typically open the terminal to `.code/claude.json` to open global settings, where there's a key called MCP servers. I pass in the Shadcn component and Shadcn theme tools so sub agents have access to them.

What I normally do is open the terminal and do `code .doc/claude` to open personal settings for Claude Code that will be applied across all projects. I create either a project-specific agent or a personal-level agent. Claude can help generate the title, description, and system prompt for the sub agent based on a quick explanation.

For example, my Shadcn agent is described as "a Shadcn frontend expert who can help design world-class frontend UI" with relevant MCP tools. I paste docs into their system prompt and attach special MCP tools with rules about how to use them.

The overall plan for the Shadcn agent includes:
1. Listing all the components
2. Choosing the right component and getting example code
3. Getting reference about how to composite different UI patterns together using blocks
4. Getting relevant themes
5. Rules about where to put which component files

I add a goal for each sub agent mentioning that the goal is to "design and propose a detailed implementation plan and never do the actual implementation." Once they finish, they should save the design file to `.doc/claude/docs`.

I also include an output format instructing that the final message should look like: "I've created a plan as this file, please read that first before you proceed." This message will be sent back to the Claude Code parent agent.

I include these rules across all sub agents:
- Don't actually do the implementation
- Before you do any work, look at the context file first to get full context
- After finishing your work, update this context file

For the Vercel AI SDK expert, I have the same structure for output format and rules. The only difference is I include more detailed documentation about the latest Vercel AI SDK docs, which I grabbed directly from their website - fundamental important pages about Vercel AI SDK v5 plus a migration guide that clearly spells out the difference between 4.0 and 5.0.

## Demo Results

When I tested this with building a ChatGPT replica using Shadcn for the frontend and Vercel AI SDK for the AI service, the results were impressive:

1. The parent agent created a context session file to document the project
2. It triggered the Shadcn agent with specific tasks and context file reference
3. The Shadcn agent read the context file, used MCP tools to retrieve components and examples
4. It created detailed UI design documentation with overall layout and planned components
5. The parent agent read the plan and broke down the actual implementation
6. The result was extremely high fidelity with detailed interactions, looking almost identical to the first version of ChatGPT
7. For the Vercel SDK integration, the process repeated - the sub agent researched and created an implementation plan, the parent agent executed it
8. The final application worked in one shot

This approach ensures all execution is done by the parent agent who has full context, making it much easier to fix issues when they arise.

---

*This content discusses best practices for using sub agents as researchers rather than implementers, leveraging file-system-based context management to dramatically improve AI coding workflows.*
