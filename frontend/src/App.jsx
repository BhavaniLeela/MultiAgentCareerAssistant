import { useState } from "react";
import {
  Sparkles,
  Brain,
  Target,
  FolderKanban,
  Map,
  ArrowRight,
  LoaderCircle,
  RotateCcw,
  CheckCircle2,
  AlertCircle,
} from "lucide-react";

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
  function App() {
  const [careerGoal, setCareerGoal] = useState("");
  const [skills, setSkills] = useState("");
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyzeCareer(event) {
    event.preventDefault();

    setLoading(true);
    setError("");
    setReport(null);

    const userRequest = `
      My target career role is: ${careerGoal}

      My existing technical skills are: ${skills}

      Analyze my skills, identify missing skills,
      recommend a practical project, and create
      a learning roadmap for my career goal.
    `;

    try {
      const response = await fetch(`${API_URL}/career/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_request: userRequest,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to analyze your career."
        );
      }

      setReport(data);
    } catch (err) {
      setError(
        err.message ||
        "Could not connect to the backend. Check whether FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  }

  function resetForm() {
    setCareerGoal("");
    setSkills("");
    setReport(null);
    setError("");
  }

  return (
    <div className="min-h-screen bg-[#0b0718] text-white">

      {/* Navigation */}
      <nav className="border-b border-white/10 px-6 py-5">
        <div className="mx-auto flex max-w-6xl items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="rounded-xl bg-purple-600 p-2">
              <Brain size={23} />
            </div>

            <div>
              <h1 className="text-lg font-bold">
                CareerAI
              </h1>
              <p className="text-xs text-purple-300">
                Multi-Agent Career Assistant
              </p>
            </div>
          </div>

          <span className="rounded-full border border-purple-400/30 px-3 py-1 text-xs text-purple-300">
            AI Powered
          </span>
        </div>
      </nav>

      {/* Main section */}
      <main className="mx-auto max-w-5xl px-6 py-12">

        <div className="mb-10 text-center">
          <div className="mb-4 inline-flex items-center gap-2 rounded-full bg-purple-500/10 px-4 py-2 text-sm text-purple-300">
            <Sparkles size={16} />
            Powered by Agentic AI
          </div>

          <h2 className="text-4xl font-bold leading-tight md:text-5xl">
            Build Your Career
            <span className="block text-purple-400">
              With AI Guidance
            </span>
          </h2>

          <p className="mx-auto mt-4 max-w-2xl text-gray-400">
            Discover your skill gaps, get project recommendations,
            and create a personalized learning roadmap using
            intelligent AI agents.
          </p>
        </div>

        {/* Feature cards */}
        <div className="mb-10 grid gap-4 md:grid-cols-3">

          <FeatureCard
            icon={<Target />}
            title="Skill Analysis"
            description="Identify your strengths and missing skills."
          />

          <FeatureCard
            icon={<FolderKanban />}
            title="Project Ideas"
            description="Find projects that strengthen your portfolio."
          />

          <FeatureCard
            icon={<Map />}
            title="Learning Roadmap"
            description="Get a structured path toward your career goal."
          />

        </div>

        {/* Input form */}
        <div className="rounded-2xl border border-purple-500/20 bg-[#151025] p-6 shadow-xl shadow-purple-950/20 md:p-8">

          <div className="mb-6">
            <h3 className="text-xl font-semibold">
              Tell us about yourself
            </h3>

            <p className="mt-2 text-sm text-gray-400">
              Enter your career goal and current technical skills.
            </p>
          </div>

          <form onSubmit={analyzeCareer} className="space-y-5">

            <div>
              <label className="mb-2 block text-sm font-medium">
                Target Career Role
              </label>

              <input
                type="text"
                required
                minLength={2}
                placeholder="Example: AI Engineer"
                value={careerGoal}
                onChange={(e) => setCareerGoal(e.target.value)}
                className="w-full rounded-xl border border-white/10 bg-[#0d0919] px-4 py-3 outline-none transition focus:border-purple-500"
              />
            </div>

            <div>
              <label className="mb-2 block text-sm font-medium">
                Your Existing Skills
              </label>

              <textarea
                required
                minLength={3}
                rows={4}
                placeholder="Example: Python, Machine Learning, Deep Learning, RAG, LangChain..."
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
                className="w-full resize-y rounded-xl border border-white/10 bg-[#0d0919] px-4 py-3 outline-none transition focus:border-purple-500"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="flex w-full items-center justify-center gap-2 rounded-xl bg-purple-600 px-5 py-3 font-semibold transition hover:bg-purple-500 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? (
                <>
                  <LoaderCircle className="animate-spin" size={19} />
                  Analyzing Your Career...
                </>
              ) : (
                <>
                  Analyze My Career
                  <ArrowRight size={19} />
                </>
              )}
            </button>

          </form>

          {error && (
            <div className="mt-5 flex gap-3 rounded-xl border border-red-500/20 bg-red-500/10 p-4 text-sm text-red-300">
              <AlertCircle className="shrink-0" size={20} />
              <p>{error}</p>
            </div>
          )}

        </div>

        {/* Result section */}
        {report && (
          <section className="mt-10 rounded-2xl border border-green-500/20 bg-[#151025] p-6 md:p-8">

            <div className="mb-6 flex flex-wrap items-center justify-between gap-3">
              <div>
                <div className="mb-2 flex items-center gap-2 text-green-400">
                  <CheckCircle2 size={19} />
                  <span className="text-sm font-medium">
                    Analysis completed
                  </span>
                </div>

                <h3 className="text-2xl font-bold">
                  Your Career Report
                </h3>

                <p className="mt-1 text-sm text-purple-300">
                  Target Role: {report.target_role}
                </p>
              </div>

              <button
                onClick={resetForm}
                className="flex items-center gap-2 rounded-lg border border-white/10 px-4 py-2 text-sm text-gray-300 transition hover:bg-white/5"
              >
                <RotateCcw size={16} />
                Start Again
              </button>
            </div>

            <div className="rounded-xl border border-white/10 bg-[#0d0919] p-5">
              <pre className="whitespace-pre-wrap break-words font-sans text-sm leading-7 text-gray-300">
                {report.final_report}
              </pre>
            </div>

          </section>
        )}

        {/* Loading message */}
        {loading && (
          <div className="mt-6 text-center text-sm text-purple-300">
            Your AI agents are working together. This may take a little time.
          </div>
        )}

      </main>

      <footer className="border-t border-white/10 px-6 py-6 text-center text-sm text-gray-500">
        Built with React, FastAPI, LangGraph and Groq
      </footer>

    </div>
  );
}


function FeatureCard({ icon, title, description }) {
  return (
    <div className="rounded-xl border border-purple-500/20 bg-[#151025] p-5">
      <div className="mb-3 inline-flex rounded-lg bg-purple-500/15 p-3 text-purple-400">
        {icon}
      </div>

      <h3 className="font-semibold">{title}</h3>

      <p className="mt-2 text-sm leading-6 text-gray-400">
        {description}
      </p>
    </div>
  );
}

export default App;