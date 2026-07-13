Create one horizontal look-direction strip for Codex pet `reef`, atlas row 9.

SCALE LOCK IS A HARD REQUIREMENT: all eight Reef figures must have the same full-body height, shoulder width, head size, foot spacing, and lower-body baseline as one another. Do not progressively shrink poses 5-8. The `135` and `157.5` figures must be exactly as large and broad as `000`, `090`, and the approved cardinal references; only the eyes, muzzle, head, neck, cap perspective, and tiny upper-chest follow-through may change.

FIXED-BODY STRATEGY: treat the eight bodies as the same locked standing construction redrawn consistently. Keep shoulders, chest outline, arms, hands, shorts, thighs, feet, dorsal-fin base, tail root, and overall silhouette in the same positions and at the same scale in all eight slots. Do not rotate or narrow the torso. Animate direction only through complete-eye rotation, eyelids/brows, long muzzle yaw/pitch, head/neck turn, and rigid cap perspective. Make slot 1 `000` directly match the approved `000` cardinal family: head tipped back, muzzle visibly aimed above the head center, pupils/eye surfaces visibly up, more underside of jaw visible; it must not resemble neutral/front.

LOOP-BOUNDARY REPAIR: use the attached completed row 10 as the authoritative physical-size and center reference. Every row-9 body must match row 10's `337.5` and `180` body height, torso width, shoulder width, limb size, foot spacing, tail-root position, center, and baseline. Slot `000` must be exactly one same-scale, same-center step after row-10 `337.5`; do not enlarge it to match the cardinal strip's source body size—borrow only the approved upward head/eye meaning. Slot `157.5` must be one same-scale, same-center step before row-10 `180`.

RIGHT-SIDE SEMANTIC LOCK: after centered `000`, every pose from `022.5` through `157.5` stays on the viewer's SCREEN-RIGHT half. In every one of those seven poses, the nose tip and visible eye/pupil surface must remain to the screen-right side of the head center. Never flip the muzzle to screen-left at `090`, `112.5`, `135`, or `157.5`. `045` and `067.5` establish the correct right-facing side; `090` continues that same side at maximum right turn; `112.5` and `135` keep the same right turn while pitching down; `157.5` keeps a subtle but still visible right cue before centered `180`. Do not mirror any individual pose.

COMPACT SILHOUETTE REPAIR: the current registered row-9 `157.5` body and the final row-10 bodies are the required outer-size template, approximately the same compact ~10k-pixel silhouette. Redraw ALL eight row-9 bodies with that compact `157.5` shoulder width, torso width, arm/leg thickness, head size, foot spacing, center, and baseline. The current larger `000` construction is explicitly rejected: do not enlarge its head, shoulders, chest, arms, legs, feet, or tail. `000` must keep the exact compact body silhouette of `157.5` and row-10 `337.5`; express up only through complete-eye rotation, eyelids, muzzle pitch, small neck motion, and cap perspective inside the same outer dimensions.

NUMERIC CORRECTION TARGET: compared with the rejected current `000`, draw the new `000` about 15% smaller in visible whole-body area and move its body center about 9 pixels toward the row-10 `337.5` center. Reduce shoulder span, chest/arm bulk, leg/foot size, tail span, and head outer size together—not just the muzzle. At final cell size, the outer silhouette and bounding box of new `000` and row-10 `337.5` must visually overlay except for the one-step up-left-to-up head/eye change. Keep this compact size through `022.5`–`157.5`.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip is authoritative for the up, screen-right, down, and screen-left pose families. Interpolate the intermediate directions as even 22.5-degree steps between those anchors.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-right means the viewer's right image edge, never the character's own right. The row should travel naturally through the right half of the loop. Near-vertical 022.5 and 157.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.
