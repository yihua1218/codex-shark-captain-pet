Create Codex v2 pet look row 9 for `reef` as exactly 8 full-body frames in this order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5.

SCALE LOCK IS A HARD REQUIREMENT: all eight Reef figures must have the same full-body height, shoulder width, head size, foot spacing, and lower-body baseline. Do not progressively shrink the down-right poses. `135` and `157.5` must match the physical size of `000` and `090`; change gaze and head/neck orientation only.

FIXED-BODY STRATEGY: redraw one identical standing body construction in every slot. Lock shoulders, chest, arms, hands, shorts, legs, feet, tail root, body height, width, and baseline. Do not turn or narrow the torso. Change only complete eyes, eyelids/brows, muzzle yaw/pitch, head/neck, and rigid cap perspective. Slot 1 must visibly match the approved upward cardinal with head tipped back, muzzle aimed up, upward eye surfaces, and visible jaw underside—not a neutral front pose.

LOOP-BOUNDARY REPAIR: the attached completed row 10 controls physical size and center. Match every row-9 body to row-10 `337.5` and `180` height, torso/shoulder width, limbs, foot spacing, tail root, center, and baseline. `000` is one same-scale step after `337.5`; `157.5` is one same-scale step before `180`. Use the cardinal strip only for gaze meaning, not its larger source-body size.

RIGHT-SIDE SEMANTIC LOCK: `022.5`, `045`, `067.5`, `090`, `112.5`, `135`, and `157.5` must all keep the nose tip and visible eye/pupil surface on the viewer's screen-right side of the head center. No mid-row mirror or left-facing flip. `090` is maximum right; later poses stay right while pitching down, and `157.5` retains a subtle right cue before centered `180`.

COMPACT SILHOUETTE REPAIR: use current registered row-9 `157.5` and final row-10 bodies as the outer-size template for every row-9 pose. Keep their compact shoulder/torso width, limb thickness, head size, feet, center, and baseline. Reject the oversized current `000`; `000` must use the same compact outer body and show up only through eyes, eyelids, muzzle pitch, neck, and cap perspective.

NUMERIC CORRECTION TARGET: make new `000` about 15% smaller in whole-body visible area than the rejected current `000`, with its center shifted about 9 pixels toward row-10 `337.5`. Reduce shoulders, chest, arms, legs, feet, tail, and head together. Its final outer silhouette must visually overlay row-10 `337.5` except for one head/eye direction step, and this compact size continues through the full row.

Use the canonical base, standard contact sheet, layout guide, approved four-cardinal strip, and `qa/look-mechanics.md`. Draw the complete eight-pose row as one coherent animation family, interpolating even 22.5-degree steps between the cardinal pose families. Keep the same pet identity, face construction, materials, palette, markings, and props. Each direction must read correctly at pet size and join continuously at the 000 and 180 boundaries.

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

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Use a flat pure green #00FF00 background. One complete unclipped pose per invisible slot. No whole-sprite rotation, replacement eyes, labels, guide marks, shadows, glows, scenery, detached effects, or #00FF00 colors in the pet.
