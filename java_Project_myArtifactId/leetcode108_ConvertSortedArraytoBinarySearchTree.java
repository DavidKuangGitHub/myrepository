import java.util.Arrays;

/*leetcode108_ConvertSortedArraytoBinarySearchTree.java
Requirement: Given an array where elements are sorted in ascending order, convert it to a height balanced BinarySearchTree.
Note: For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example: One sorted array: [-10, -3, 0, 5, 0]
One possible answer:[0,-3,9,-10,null, 5] 
     0
   -3    9
 -10   5  
*/
public class leetcode108_ConvertSortedArraytoBinarySearchTree {
	
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length==0){ return null; }
        int mid = nums.length/2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid));
        node.right = sortedArrayToBST(Arrays.copyOfRange(nums, mid+1, nums.length));
        return node;
    }
	/*public TreeNode sortedArrayToBST(int[] nums) 
    {
      TreeNode root=null;
      
      if(nums.length==0)
      return root;
        
      if(nums.length==1)
      {
      root=new TreeNode();
      root.val=nums[0];
      root.left=null;
      root.right=null;
      return root;
      }
      
      root=new TreeNode();
      int low=0,high=nums.length-1;
      int mid=(low+high)/2;
      root.val=nums[mid];
      
      if(mid-1<low&&mid+1<=high)
      helper(root,mid+1,high,nums);
        
      else if(mid-1>=low&&mid+1>high)
      helper(root,low,mid-1,nums);
        
      else if(mid-1>=low&&mid+1<=high)
      {
      helper(root,low,mid-1,nums);
      helper(root,mid+1,high,nums);
      }
      
      return root;
    }
    
    public void helper(TreeNode root,int x,int y,int nums[])
    {
        int low=x;
        int high=y;
        int mid=(low+high)/2;
        
        TreeNode node=new TreeNode();
        
         if(nums[mid]<=root.val)
        {node.val=nums[mid];
         root.left=node;
        }
        
        else if(nums[mid]>root.val)
        {
        node.val=nums[mid];
        root.right=node;
        }
        
        root=node;
        
        if(mid-1<low&&mid+1<=high)
        helper(root,mid+1,high,nums);
        
        else if(mid-1>=low&&mid+1>high)
        helper(root,low,mid-1,nums);
        
        else if(mid-1>=low&&mid+1<=high)
        {
        helper(root,low,mid-1,nums);
        helper(root,mid+1,high,nums);
        }
    
        return;
    }*/
	//static TreeNode root;
    
    public static void main(String[] args) {
    	leetcode108_ConvertSortedArraytoBinarySearchTree mylc108_CSAtBST= new leetcode108_ConvertSortedArraytoBinarySearchTree();
    	int[] myNums = {-10, -3, 0, 5, 0};
    	TreeNode myTree = mylc108_CSAtBST.sortedArrayToBST(myNums);
		/*for(String path: myTree) {
			System.out.println(path);
		}*/
    	//myTree.printTree();
    	
    }

}