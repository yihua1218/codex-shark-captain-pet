Create one horizontal animation strip for Codex pet `reef`, state `running-left`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Reef is a mature muscular anthropomorphic blue tiger shark captain. Preserve the white captain cap with navy brim and brass band, deep-blue tiger stripes, pale blue chest and abdomen, powerful but compact sailor build, dorsal fin, thick tail with shark caudal fin, confident friendly toothy grin, and dark navy deck shorts with a restrained red-blue plaid accent. His permanent maritime identity props are a compact brass-and-navy ship wheel, a coiled rope, and a brass spyglass; use only the prop relevant to each state, always physically touching his hands or body. No scenery, ocean, boat hull, text, logos, shadows, floating effects, or detached objects.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Polished clean 2D cel-shaded mascot illustration matching the supplied reference: crisp dark outlines, cool ocean-blue palette, readable large forms, consistent mature friendly captain persona, non-explicit..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Brisk sailor deck-hurry loop traveling screen-left: Reef faces left and alternates a compact sea-legged stride while carrying one neatly coiled mooring rope hugged securely against his torso. The rope must remain one connected opaque component touching both hands and body in every frame.

State requirements:
- Show directional drag movement to the left through body, limb, and prop movement only.
- The row must unmistakably face and travel left.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
