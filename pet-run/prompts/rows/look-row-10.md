Create one horizontal look-direction strip for Codex pet `reef`, atlas row 10.

FIXED-BODY AND SCALE LOCK: use the completed row 9 as the exact body-size and registration standard. All eight Reef figures must keep the same full-body height, shoulder width, head size, foot spacing, lower-body baseline, torso outline, arms, shorts, legs, feet, dorsal-fin base, and tail root as approved row 9 and as one another. Animate direction only through complete-eye rotation, eyelids/brows, long muzzle yaw/pitch, head/neck turn, and rigid cap perspective. Do not progressively shrink poses toward `337.5`. The final `337.5` must be one even step before approved `000` in both direction and physical scale.

CROSS-ROW BOUNDARY LOCK: the attached REGISTERED row 9 is the authoritative geometry, size, center, and baseline reference, overriding the raw cardinal source size. Slot `180` must reuse the same planted body construction, torso/shoulder width, limb size, foot spacing, center, and baseline as row-9 `157.5`, changing only the head/eyes from right-down to centered-down by one step. Slot `337.5` must reuse the same planted body construction, torso/shoulder width, limb size, foot spacing, center, and baseline as row-9 `000`, changing only the head/eyes from up-left to centered-up by one step. Interpolate the same body construction across all row-10 slots; do not introduce a second character scale or gradually shrink the body.

LEFT-SIDE SEMANTIC LOCK: after centered `180`, every pose from `202.5` through `337.5` stays on the viewer's SCREEN-LEFT half. In every one of those seven poses, the nose tip and visible eye/pupil surface must remain to the screen-left side of the head center. Never flip the muzzle to screen-right at `225`, `247.5`, `270`, `292.5`, `315`, or `337.5`. `270` must match the approved unmistakable left cardinal. `292.5`, `315`, and `337.5` keep the same left-facing side while pitching upward; `337.5` retains a subtle but definite left cue before centered `000`. Do not mirror any individual pose.

FINAL-CELL EDGE LOCK: the new registered row 9 sets a larger shared scale, so keep every row-10 source pose laterally compact with generous chroma-only padding on both sides. Pull elbows, arms, hands, tail tip, hat brim, and muzzle inward without changing direction meaning. `202.5` previously touched the final cell edge and is rejected; redraw it and all other poses narrow enough that deterministic registration leaves zero non-transparent pixels near every final cell edge.

NUMERIC CLOSURE INTERPOLATION: keep `180` at the current row-9 `157.5` compatible body and center. Then make seven equal, subtle physical interpolation steps so `337.5` exactly matches row-9 `000` outer body silhouette and center. The rejected current `337.5` is about 14% too small in visible whole-body area and about 9.6 pixels off-center relative to `000`; distribute that correction evenly, roughly 2% visible-area growth and 1.4 pixels of center travel per direction step. By `337.5`, shoulders, arms, torso, thighs, feet, tail root, head outer size, bounding box, and center must visually overlay row-9 `000`, with only the one-step up-left versus up head/eye difference. Keep lateral limbs tucked so this endpoint still has safe cell padding.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip and completed coherent row 9 are authoritative. Use the cardinals for direction meaning and row 9 for cross-row identity, scale, registration, and continuity.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `180`: vertical DOWN; no horizontal requirement.
2. `202.5`: horizontal SCREEN-LEFT and vertical DOWN.
3. `225`: horizontal SCREEN-LEFT and vertical DOWN.
4. `247.5`: horizontal SCREEN-LEFT and vertical DOWN.
5. `270`: horizontal SCREEN-LEFT; no vertical requirement.
6. `292.5`: horizontal SCREEN-LEFT and vertical UP.
7. `315`: horizontal SCREEN-LEFT and vertical UP.
8. `337.5`: horizontal SCREEN-LEFT and vertical UP.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-left means the viewer's left image edge, never the character's own left. The row should travel naturally through the left half of the loop. Near-vertical 202.5 and 337.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.
