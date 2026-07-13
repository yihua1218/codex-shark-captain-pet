Create one horizontal animation strip for Codex pet `reef`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Reef is a mature muscular anthropomorphic blue tiger shark captain. Preserve the white captain cap with navy brim and brass band, deep-blue tiger stripes, pale blue chest and abdomen, powerful but compact sailor build, dorsal fin, thick tail with shark caudal fin, confident friendly toothy grin, and dark navy deck shorts with a restrained red-blue plaid accent. His permanent maritime identity props are a compact brass-and-navy ship wheel, a coiled rope, and a brass spyglass; use only the prop relevant to each state, always physically touching his hands or body. No scenery, ocean, boat hull, text, logos, shadows, floating effects, or detached objects.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Polished clean 2D cel-shaded mascot illustration matching the supplied reference: crisp dark outlines, cool ocean-blue palette, readable large forms, consistent mature friendly captain persona, non-explicit..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Calm low-distraction captain-at-rest loop: hands relaxed at his hips, feet planted in a steady sea-legs stance, subtle chest breathing, one tiny blink, a slight head bob, and a very small tail sway. No prop interaction.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
