Create Codex v2 pet look row 10 for `reef` as exactly 8 full-body frames in this order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5.

FIXED-BODY AND SCALE LOCK: match completed row 9's body height, shoulder width, head size, foot spacing, baseline, torso, limbs, shorts, dorsal-fin base, and tail root in every slot. Change only complete eyes, muzzle, head/neck, and cap perspective. Do not shrink toward `337.5`; it must be one same-scale step before approved `000`.

CROSS-ROW BOUNDARY LOCK: use the attached REGISTERED row 9 as the only physical geometry standard. `180` must share row-9 `157.5` body/center/baseline and differ only by one head/eye step. `337.5` must share row-9 `000` body/center/baseline and differ only by one head/eye step. Keep that same planted body construction throughout row 10; no second scale and no body shrink.

LEFT-SIDE SEMANTIC LOCK: `202.5`, `225`, `247.5`, `270`, `292.5`, `315`, and `337.5` must all keep the nose tip and visible eye/pupil surface on the viewer's screen-left side of the head center. No mid-row mirror or right-facing flip. `270` is maximum left; later poses stay left while pitching up, and `337.5` retains a definite left cue before centered `000`.

FINAL-CELL EDGE LOCK: match the new registered row-9 shared scale and keep all row-10 poses laterally compact with generous padding. Pull elbows, arms, tail tip, hat brim, and muzzle inward. The previous `202.5` edge contact must be eliminated; every registered cell needs zero near-edge foreground pixels.

NUMERIC CLOSURE INTERPOLATION: keep `180` matched to row-9 `157.5`, then apply seven even subtle steps so `337.5` matches row-9 `000`. Correct the rejected endpoint's roughly 14% whole-body area deficit and 9.6px center offset gradually—about 2% area and 1.4px center per step. At `337.5`, shoulders, torso, limbs, feet, tail root, head size, bounding box, and center overlay `000`; preserve safe lateral padding.

Use the canonical base, standard contact sheet, layout guide, approved four-cardinal strip, and `qa/look-mechanics.md`. Draw the complete eight-pose row as one coherent animation family, interpolating even 22.5-degree steps between the cardinal pose families. Keep the same pet identity, face construction, materials, palette, markings, and props. Each direction must read correctly at pet size and join continuously at the 000 and 180 boundaries.

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

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Use a flat pure green #00FF00 background. One complete unclipped pose per invisible slot. No whole-sprite rotation, replacement eyes, labels, guide marks, shadows, glows, scenery, detached effects, or #00FF00 colors in the pet.
