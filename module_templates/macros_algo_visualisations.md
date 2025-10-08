<!--
module_id: data_structures_advanced/vis_demo
author:   David Croft
email:    david.croft@warwick.ac.uk
version: 0.0.1
current_version_description: Initial version
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook
title: data_structures_advanced/vis_demo
comment:  A demo of visualisations for algorithms
estimated_time_in_minutes: 20

@onload
    window.algo_canvas_sizes = {};

    window.scanContainers = function() {
        console.log( "scan" );
        
        var containers = document.querySelectorAll('.vis-iframe-container');
        containers.forEach(scaleIframe);

        //setTimeout(scanContainers, 2000); // wait a moment for values to change
    }

    function scaleIframe(container) {
        var iframe = container.querySelector('iframe');

        // default values
        let iframeWidth = 1000;
        let iframeHeight = 500;
        let heightPadding = 160;

        if (iframe.src in window.algo_canvas_sizes) {
            iframeWidth = window.algo_canvas_sizes[iframe.src].width;
            iframeHeight = window.algo_canvas_sizes[iframe.src].height;
        }
        else {
            // try to get size from iframe content
            try {
                let innerDoc = iframe.contentDocument || iframe.contentWindow.document;
                let canvas = innerDoc.getElementById('canvas');
                iframeWidth = canvas.width;
                iframeHeight = canvas.height;
            }
            catch (e) {
                console.error('Error getting iframe content:', e);
            }
        }

        var scale = container.offsetWidth / iframeWidth;

        if( scale < 0.6 ) scale = 0.6; // minimum scale
        if( scale > 1.0 ) scale = 1.0; // maximum scale

        iframe.style.transform = 'scale(' + scale + ')';
        iframe.style.width = iframeWidth + 'px';
        iframe.style.height = (iframeHeight + heightPadding) + 'px';
        iframe.style.display = 'block';
        iframe.style.transformOrigin = '0 0';
    }

    // Run on window resize
    window.addEventListener('resize', scanContainers);
@end

@algo_vis
<div class="vis-iframe-container">
<iframe class="vis-iframe"
        src="../assets/JavascriptVisualRelease/@0.html" 
        style="border: none;">
        Your browser does not support iframes.
</iframe>

<script style="display:none;">
    window.scanContainers();
</script>
</div>
@end

@algo_attribution
Credit is given to David Galles of the University of San Francisco for the algorithm visualisations used in this module.

[https://www.cs.usfca.edu/~galles/visualization/](https://www.cs.usfca.edu/~galles/visualization/)

THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of the University of San Francisco.
@end

-->

# Instructions

Include this file in your header:

```
import: ../module_templates/macros_algo_visualisations.md
```

------------

Use the `@algo_vis` macro to include an algorithm visualisation. The macro takes one argument, which is the name of the HTML file (without the `.html` extension) in the `assets/JavascriptVisualRelease` folder. For example:

E.g. if the file is `assets/JavascriptVisualRelease/LiaBST.html`.

```markdown
@algo_vis(LiaBST)
```

-------------------

Use the `@algo_attribution` macro to include an attribution statement for the visualisations:

```markdown
Attribution
===========

@algo_attribution
```

Attribution
===========

@algo_attribution



# Sorting Algorithms 

## Bubble Sort

@algo_vis(LiaBubble)

## Selection Sort

@algo_vis(LiaSelection)

## Insertion Sort

@algo_vis(LiaInsertion)

## Shell Sort

@algo_vis(LiaShell)

## Merge Sort

@algo_vis(LiaMerge)

## Quick Sort

@algo_vis(LiaQuick)

## Bucket Sort

@algo_vis(LiaBucketSort)

## Counting Sort

@algo_vis(LiaCountingSort)

## Radix Sort

@algo_vis(LiaRadixSort)

## Heap Sort

@algo_vis(LiaHeapSort)

# Tree Algorithms

## Binary Search Tree

@algo_vis(LiaBST)

adfsdfs

sfdgdfgdsg

## AVL Trees (Balanced binary search trees)

@algo_vis(LiaAVLtree)


## Red-Black Trees

@algo_vis(LiaRedBlack)


## Splay Trees

@algo_vis(LiaSplayTree)


# Graph Algorithms


## Breadth-First Search

@algo_vis(LiaBFS)


## Depth-First Search

@algo_vis(LiaDFS)


## Connected Components

@algo_vis(LiaConnectedComponent)


## Dijkstra's Shortest Path

@algo_vis(LiaDijkstra)


## Prim's Minimum Cost Spanning Tree

@algo_vis(LiaPrim)


## Topological Sort (Using Indegree array) 

@algo_vis(LiaTopoSortIndegree)


## Topological Sort (Using DFS) 

@algo_vis(LiaTopoSortDFS)


## Floyd-Warshall (all pairs shortest paths)

@algo_vis(LiaFloyd)


## Kruskal Minimum Cost Spanning Tree Algorith

@algo_vis(LiaKruskal)


