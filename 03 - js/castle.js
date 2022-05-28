exports castle = function (){
  cylinder0(blocks.brick.red, 10, 5)
  .right(7)
  .fwd(7)
  .box0(block.cobblestone, 7, 5, 7)
  .up(5)
  .box(blocks.slab.stonebrick, 7, 1, 7)
  .box0(blocks.fence.oak, 7, 1, 7)
  .down(5)
  .right(3)
  .box(blocks.air, 1, 2, 1)
  .back(7)
  .box(196, 1, 2, 1);
 }