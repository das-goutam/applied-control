# Contributing

Thanks for helping map how control theory is used outside the lab. This list stays useful only if every entry is a real deployment, links to a primary source, and is described accurately, so please read the criteria below before opening a pull request.

## What belongs here

An entry qualifies when **all** of the following hold.

1. **It describes a deployed control system.** The controller ran on a product, a vehicle, a spacecraft, a plant, a grid, a patient, or production software. Simulation studies, benchmark results, and proposals do not qualify, however good they are.
2. **The control content is explicit.** The source explains the feedback structure, the estimator, the optimization, or the tuning, not only the outcome. Generic machine-learning deployments belong in [applied-ml](https://github.com/eugeneyan/applied-ml) unless the model closes a control loop.
3. **It is a primary or authoritative source.** Prefer the deploying organization's own paper, engineering blog, technical report, regulatory filing, or recorded talk. News coverage and secondary summaries are not accepted as entries.
4. **The link is stable.** Use a `doi.org` link, an arXiv abstract page, an agency repository page (for example NASA NTRS or OSTI), or the official blog URL. Avoid PDF mirrors on personal or third-party sites.

The four cross-cutting sections under **Resources** (surveys, deployed software, practitioner talks, books) follow the same spirit: they must help someone understand or build deployed control systems.

## How to add an entry

1. Find the data file for the domain in [`data/`](data/). Domains and their subsections are declared in [`data/_domains.yaml`](data/_domains.yaml).
2. Append an item with exactly these keys:

   ```yaml
   - title: "Exact published title"
     url: https://doi.org/10.xxxx/xxxxx
     org: [Organization A, Organization B]
     year: 2021
     type: paper          # paper | blog | report | talk | video | code | book | standard
     topic: "Launch & landing"
     methods: [MPC, Kalman filtering]
     stage: flight        # production | flight | clinical | field | operations
     summary: "One sentence in your own words, at most 35 words: what was controlled, how, and the evidence it was deployed."
   ```

3. Use method tags from [`data/_vocab.yaml`](data/_vocab.yaml). If none fits, add the new tag there with a one-line description in the same pull request.
4. Run the build, which validates every entry and regenerates the README and indexes:

   ```bash
   pip install -r requirements.txt
   python scripts/build.py
   ```

5. Commit the data change **and** the regenerated files. CI fails if the README is out of date.

## Style for summaries

- Write the summary yourself. Do not paste sentences from the abstract.
- Say what was controlled, the approach, and the deployment evidence, for example "flown on twelve test flights" or "running across all production clusters since 2019".
- Keep it neutral and specific. Avoid marketing language such as "revolutionary" or "state of the art".
- Avoid em dashes; use commas or separate sentences.

## Choosing the stage

| Stage | Use when |
|---|---|
| `production` | Shipped in a commercial product or running in production software |
| `flight` | Flown on an aircraft, spacecraft, or launch vehicle |
| `clinical` | Used in human clinical trials or in an approved medical device |
| `field` | Tested on real hardware or infrastructure outside the lab, not yet a product |
| `operations` | Running in an operating plant, grid, fleet, or facility; also used for surveys and books |

When a source reports several stages, pick the most mature one it documents.

## Reporting a problem

Open an issue for broken links, misattributed organizations, or entries that do not meet the criteria. Link rot is checked weekly by CI, and flagged links are fixed or removed.
